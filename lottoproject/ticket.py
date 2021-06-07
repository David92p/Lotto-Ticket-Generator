from .city import City
from .bet import Bet
from .extractions import ExtractionBoard

from random import sample

class Ticket:
    """The following dictionary describes a key as the type of bet made, 
    then determines through a dictionary a winning value for each amount of numbers played"""
    win_type = {
        "ambata": {1: 11.23, 2: 5.61, 3: 3.74, 4: 2.80, 5: 2.24, 6: 1.87, 7: 1.60, 8: 1.40, 9: 1.24, 10: 1.12},
        "ambo": {2: 250, 3: 83.33, 4: 41.66, 5: 25, 6: 16.66, 7: 11.90, 8: 8.92, 9: 6.94, 10: 5.55}, 
        "terno": {3: 4500, 4: 1125, 5: 450, 6: 225, 7: 128.57, 8: 80.35, 9: 53.57, 10: 37.50},
        "queterna": {4: 120000, 5: 24000, 6: 8000, 7: 3428.57, 8: 1714.28, 9: 952.28, 10: 571.42},
        "cinquina": {5: 6000000, 6: 1000000, 7: 285714.28, 8: 107142.85, 9: 47619.04, 10: 23809.52}
    }

    def __init__(self, city, bet, quantity_numbers):
        self.city = City(city)
        self.bet = Bet(bet)
        self.numbers = []
        self.numbers_generator(quantity_numbers)   
    
    def numbers_generator(self, quantity_numbers):
        numbers = list(sample(range(1, 90 + 1), quantity_numbers))
        for n in numbers:
            self.numbers.append(str(n))
        
    def print_ticket(self):
        numbers = " ".join(self.numbers)
        title = "LOTTO TICKET"
        horizontal = '+'+'-'*40+'+'
        in_line = "+"+ " "*40+"+"
        print(horizontal)
        print("|",title.center(38, " "),"|")
        print(horizontal)
        print("|"+ " "*40+"|")
        print("|",self.city.city_type.upper().center(38, " "),"|")
        print(in_line)
        print("|",self.bet.bet_type.upper().center(38, " "),"|")
        print(in_line)
        print("|"," ".join(self.numbers).center(38, " "),"|")
        print(in_line)
        print(horizontal)


    # This Function determines whether our bet was a winner or a loser
    def set_win(self):
        check = []
        for city, number in ExtractionBoard.extractions.items():
            if city == self.city.city_type:
                for i in range(len(number)):
                    for n in self.numbers:
                        if number[i] == int(n):
                            check.append(int(n))    
        if len(check) >= 1 and self.bet.bet_type == "ambata":
            return True
        elif len(check) >= 2 and self.bet.bet_type == "ambo":
            return True
        elif len(check) >= 3 and self.bet.bet_type == "terno":
            return True
        elif len(check) >= 4 and self.bet.bet_type == "quaterna":
            return True
        elif len(check) >= 5 and self.bet.bet_type == "cinquina":
            return True
        else:
            return False

    # This function returns, based on the outcome of our bet, a possible win, net of taxes to be paid, equal to 8%
    def set_win_amount(self):
        if Ticket.set_win(self):
            for form, mode in Ticket.win_type.items():
                for form, win in mode.items():
                    if form == len(self.numbers):
                        tax = (win * 8) / 100
                        amount = win - tax
                        return f'Congratulations, you have a winning ticket of € {round(amount, 2)}'

        else:
            return 'Sorry, this ticket has no winnings'
        
        

#test
if __name__ == "__main__":
    board = ExtractionBoard
    ticket1 = Ticket("venezia", "  AmbaTa  ", 10)
    ticket2 = Ticket("RoMa ", "quAterNA", 7)
    ExtractionBoard.print_board(board)
    print()
    Ticket.print_ticket(ticket1)
    print(Ticket.set_win_amount(ticket1))
    print()
    Ticket.print_ticket(ticket2)
    print(Ticket.set_win_amount(ticket2))
    

