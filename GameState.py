class GameState:
    def __init__(self):
        self.budget_raised = 0  
        self.budget_goal = 100000
        self.board_trust = 50  
        self.scandal_index = 0  
        self.turn = 1  
        self.max_turns = 5

    def show_dashboard(self):
        """Prints the current startup status to the screen in a visual way."""
        print("\n" + "=" * 50)
        print(f" 📊 STATUS BOARD — TURN {self.turn} / {self.max_turns}")
        print("=" * 50)
        print(
            f" 💰 Budget Raised:   €{self.budget_raised:,} /"
            f" €{self.budget_goal:,}"
        )
        print(f" 🤝 Board Trust:  {self.board_trust}%")
        print(f" 🚨 Scandal Index:    {self.scandal_index}%")
        print("=" * 50 + "\n")
        

    def update_state(self, delta_budget=0, delta_trust=0, delta_scandal=0):
        """Updates the game metrics by applying the deltas (positive or negative)."""
        self.budget_raised += delta_budget

        self.board_trust+=delta_trust
        if self.board_trust > 100:
            self.board_trust=100

        if self.board_trust < 0:
            self.board_trust=0

        self.scandal_index+=delta_scandal
        if self.scandal_index > 100:
            self.scandal_index=100

        self.turn += 1

    def print_parameter_changes(self, delta_budget, delta_trust, delta_scandal):
        print("=" * 50)
        print(f"Funds invested by the agent: {delta_budget}")
        print(f"{'Trust bonus: +' if delta_trust>0 else 'Trust penalty:'} {delta_trust}%")
        print(f"{'Scandal index increase: +' if delta_scandal>0 else 'Scandal index reduction:'} {abs(delta_scandal)}%")
        print("=" * 50)
        return None

    def check_game_over(self):
        """Checks if the game is over (Victory or Defeat).

        Returns: - 'VICTORY' - 'DEFEAT' - None (game continues)
        """
        if self.budget_raised >= self.budget_goal:
            return "VICTORY"

        if self.board_trust <= 0:
            return "DEFEAT_TRUST"

        if self.scandal_index >= 100:
            return "DEFEAT_SCANDAL"

        if self.turn > self.max_turns:
            return "DEFEAT_TURNS"

        return None

    
        