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

    # update dello stato del gioco prima del prossimo turno
    game.aggiorna_stato(feedback['delta_budget'], feedback['delta_fiducia'], feedback['delta_scandalo'])
    
    print("=" * 50)
    print(f"Soldi investiti dall'agente: {feedback['delta_budget']}")
    print(f"{'Bonus di fiduca: +' if feedback['delta_fiducia']>0 else 'Penalità di fiduca:'} {feedback['delta_fiducia']}%")
    print(f"{'Aumento indice di scandalo: +' if feedback['delta_scandalo']>0 else 'Riduzione indice di scandalo:'} {abs(feedback['delta_scandalo'])}%")
    print("=" * 50)




    # verifica se il gioco è finito
    risultato = game.verifica_fine_partita()
    if risultato:
        print(f"\nGAME OVER: {risultato}")
        break

