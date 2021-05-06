class TicketType:
     # Class variable containing the possible bets elements:
    bets = ["ambata", "ambo", "terno", "quaterna", "cinquina"]

    def __init__(self, bet):
        bet = bet.strip().lower()
        if TicketType.check_bet(bet):
            self.bet_type = bet
        else:
            return None

    # The following function returns a boolean parameter when it has been entered correctly
    @staticmethod
    def check_bet(bet):
        bet = bet.strip().lower()
        if bet in TicketType.bets:
            return True
        else:
            print('Incorrect value')
            return False

# test
if __name__ == "__main__":
    bet = TicketType("AmbaTa  ")
    print(bet)