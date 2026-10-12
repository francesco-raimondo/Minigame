from openai import OpenAI
import json
from Tools.agente_finanziere_tools import agente_finanziere_tools

class AgenteFinanziere:
    def __init__(self, base_url="http://192.168.1.100:1234/v1", model_name="qwen/qwen3-4b-2507"):
        self.client = OpenAI(base_url=base_url, api_key="not-needed")
        self.model_name = model_name
        self.system_prompt = ("Sei Mr. Sterling, un membro del consiglio d'amministrazione di una startup,"
        " investitore spietato e cinico. Ti interessano solo i dati finanziari,"
        " il ROI, i costi e la scalabilità. Disprezzi le idee vaghe o troppo"
        " idealiste. Parla in modo formale e severo in italiano. Alla fine del"
        " tuo commento, esprimi chiaramente se voti a favore o contro il"
        " finanziamento."
        )

    def valuta_pitch(self, pitch_utente, game_state):
        """Invia il pitch dell'utente e lo stato del gioco all'LLM locale."""

        # Costruiamo il contesto unendo lo stato attuale del gioco e la proposta
        prompt = (
            f"[STATO ATTUALE STARTUP]\n"
            f"- Budget raccolto finora: €{game_state.budget_ottenuto}/€{game_state.budget_obiettivo}\n"
            f"- Fiducia del board: {game_state.fiducia_board}%\n"
            f"- Turno: {game_state.turno}/{game_state.max_turni}\n\n"
            f"Ecco la mia proposta:\n\"{pitch_utente}\""
        ) 

        # Chiamata al client passando i tools importati dal file esterno
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ],
            tools=agente_finanziere_tools,
            tool_choice="required",
            temperature=0.2
        )
        # sta venendo chiamato un tool, quindi la risposta dell'agente sarà negli argomenti del tool, in questo caso in "motivazione"
        message = response.choices[0].message
        
        if message.tool_calls:
            tool_call = message.tool_calls[0]
            name_function=tool_call.function.name

            if name_function == "gestisci_decisione_board":
                # Convertiamo gli argomenti JSON restituiti dalla LLM in un dizionario Python
                arguments = json.loads(tool_call.function.arguments)
                print("DEBUG : ", arguments)
                return arguments

        else:
            print("Errore, non è stato chiamato alcun tool dall'agente finanziere")


