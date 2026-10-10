class GameState:
    def __init__(self):
        self.budget_ottenuto = 0  
        self.budget_obiettivo = 100000
        self.fiducia_board = 50  
        self.indice_scandalo = 0  
        self.turno = 1  
        self.max_turni = 5

    def show_dashboard(self):
        """Stampa a schermo lo stato attuale della startup in modo visivo."""
        print("\n" + "=" * 50)
        print(f" 📊 STATUS BOARD — TURNO {self.turno} / {self.max_turni}")
        print("=" * 50)
        print(
            f" 💰 Budget Raccolto:   €{self.budget_ottenuto:,} /"
            f" €{self.budget_obiettivo:,}"
        )
        print(f" 🤝 Fiducia del Board:  {self.fiducia_board}%")
        print(f" 🚨 Indice Scandalo:    {self.indice_scandalo}%")
        print("=" * 50 + "\n")
        

    def aggiorna_stato(self, delta_budget=0, delta_fiducia=0, delta_scandalo=0):
        """Aggiorna le metriche di gioco applicando i delta (positivi o negativi)."""
        self.budget_ottenuto += delta_budget

        self.fiducia_board+=delta_fiducia
        if self.fiducia_board > 100:
            self.fiducia_board=100

        self.indice_scandalo+=delta_scandalo
        if self.indice_scandalo > 100:
            self.indice_scandalo=100

        self.turno += 1

    def verifica_fine_partita(self):
        """Controlla se il gioco è finito (Vittoria o Sconfitta).

        Restituisce: - 'VITTORIA' - 'SCONFITTA' - None (il gioco continua)
        """
        if self.budget_ottenuto >= self.budget_obiettivo:
            return "VITTORIA"

        if self.fiducia_board <= 0:
            return "SCONFITTA_FIDUCIA"

        if self.indice_scandalo >= 100:
            return "SCONFITTA_SCANDALO"

        if self.turno > self.max_turni:
            return "SCONFITTA_TURNI"

        return None

    
        