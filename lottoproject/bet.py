class Bet:
     # Class variable containing the possible bets elements:
    bets = ["ambata", "ambo", "terno", "quaterna", "cinquina"]

    def __init__(self, bet):
        bet = bet.strip().lower()
        self.bet_type = None
        if Bet.check_bet(bet):
            self.bet_type = bet

    # The following function returns a boolean parameter when it has been entered correctly
    @staticmethod
    def check_bet(bet):
        bet = bet.strip().lower()
        if bet in Bet.bets:
            return True
        else:
            print('Incorrect value')
            return False

    def __str__(self):
        return self.bet_type

# test
if __name__ == "__main__":
    bet = Bet("AmbaTa  ")
    print(bet)