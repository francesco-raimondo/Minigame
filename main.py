from GameState import GameState
from Agents.FinancierAgent import FinancierAgent

game = GameState()
sterling = FinancierAgent()

for i in range (1,6):
    game.show_dashboard()
     # check if the game is over
    result = game.check_game_over()
    if result:
        print(f"\nGAME OVER: {result}")
        break

    pitch = input("Enter your startup pitch: ")
    print("Mr. Sterling is evaluating...")
    feedback = sterling.evaluate_pitch(pitch, game)
    print("\n" + "=" * 50)
    print("Mr. Sterling's Feedback:")
    print(f"Outcome: {'APPROVED' if feedback['favorable_vote'] else 'REJECTED'}")
    print(f"Mr. Sterling: \"{feedback['motivation']}\"")

    
    game.print_parameter_changes(feedback['delta_budget'], feedback['delta_trust'], feedback['delta_scandal'])

    # update game state before the next turn
    game.update_state(feedback['delta_budget'], feedback['delta_trust'], feedback['delta_scandal'])
    




   
