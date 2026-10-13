from GameState import GameState
from Agents.AgenteFinanziere import AgenteFinanziere

game = GameState()
sterling = AgenteFinanziere()

for i in range (1,6):
    game.show_dashboard()
    pitch = input("Inserisci il tuo pitch per la startup: ")
    print("Mr. Sterling sta valutando...")
    feedback = sterling.valuta_pitch(pitch, game)
    print("\n" + "=" * 50)
    print("Feedback di Mr. Sterling:")
    print(f"Esito: {'APPROVATO' if feedback['voto_favorevole'] else 'BOCCIATO'}")
    print(f"Mr. Sterling: \"{feedback['motivazione']}\"")

    
    game.stampa_modifiche_parametri(feedback['delta_budget'], feedback['delta_fiducia'], feedback['delta_scandalo'])

    # update dello stato del gioco prima del prossimo turno
    game.aggiorna_stato(feedback['delta_budget'], feedback['delta_fiducia'], feedback['delta_scandalo'])
    



    # verifica se il gioco è finito
    risultato = game.verifica_fine_partita()
    if risultato:
        print(f"\nGAME OVER: {risultato}")
        break

