from GameState import GameState

game=GameState()


delta=20


for i in range(5):
    game.show_dashboard()
    game.aggiorna_stato(delta_budget=delta, delta_fiducia=-5, delta_scandalo=40)
    result=game.verifica_fine_partita()

    if result:
        print(f"Game Over: {result}")
        break

