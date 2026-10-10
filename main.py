from GameState import GameState
from Agents.AgenteFinanziere import AgenteFinanziere

game = GameState()
sterling = AgenteFinanziere()

game.show_dashboard()
pitch = input("Inserisci il tuo pitch per la startup: ")
print("Mr. Sterling sta valutando...")
feedback = sterling.valuta_pitch(pitch, game)
print("\n" + "=" * 50)
print("Feedback di Mr. Sterling:")
print(feedback)

