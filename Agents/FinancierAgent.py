from openai import OpenAI
import json
from Tools.financier_agent_tools import financier_agent_tools
from dotenv import load_dotenv
import os

load_dotenv()  # automatically loads .env from the project root
BASE_URL = os.getenv("BASE_URL")
API_KEY  = os.getenv("API_KEY")
MODEL    = os.getenv("MODEL")




class FinancierAgent:
    def __init__(self, base_url=BASE_URL, model_name=MODEL, api_key=API_KEY):
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.model_name = model_name
        self.system_prompt = ("You are Mr. Sterling, a board member of a startup,"
        " a ruthless and cynical investor. You only care about financial data,"
        " ROI, costs and scalability. You despise vague or overly"
        " idealistic ideas. Speak formally and sternly in English. At the end of"
        " your comment, clearly state whether you vote in favour or against"
        " funding."
        )

    def evaluate_pitch(self, user_pitch, game_state):
        """Sends the user's pitch and the game state to the local LLM."""

        # We build the context by combining the current game state and the proposal
        prompt = (
            f"[CURRENT STARTUP STATUS]\n"
            f"- Budget raised so far: €{game_state.budget_raised}/€{game_state.budget_goal}\n"
            f"- Board trust: {game_state.board_trust}%\n"
            f"- Turn: {game_state.turn}/{game_state.max_turns}\n\n"
            f"Here is the user's proposal:\n\"{user_pitch}\""
        ) 

        # Call to the client passing the tools imported from the external file
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ],
            tools=financier_agent_tools,
            tool_choice="required",
            temperature=0.2
        )
        # a tool is being called, so the agent's response will be in the tool arguments, in this case in "motivation"
        message = response.choices[0].message
        
        if message.tool_calls:
            tool_call = message.tool_calls[0] # message.tool_calls is a list because a LLM can call more than one tool (chain of tools), in this case is eleected only [0] (only one tool)
            function_name=tool_call.function.name

            if function_name == "handle_board_decision":
                # We convert the JSON arguments returned by the LLM into a Python dictionary
                arguments = json.loads(tool_call.function.arguments)
                return arguments

            elif function_name == "issue_penalty":
                # We convert the JSON arguments returned by the LLM into a Python dictionary
                arguments = json.loads(tool_call.function.arguments)
                return arguments

        else:
            print("Error: no tool was called by the financier agent")


