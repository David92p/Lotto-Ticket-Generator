from .city import City
from .bet import Bet
from .extractions import ExtractionBoard

from random import sample

class Ticket:
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


    # Function that checks the numbers of our tickets with the general scoreboard
    def set_win(self):
        check = []
        for city, number in ExtractionBoard.extractions.items():
            if city == self.city.city_type:
                for i in range(len(number)):
                    for n in self.numbers:
                        if number[i] == int(n):
                            check.append(int(n))    
        if len(check) >= 1 and self.bet.bet_type == "ambata":
            return "Congratulations, it's a winning ticket!"
        elif len(check) >= 2 and self.bet.bet_type == "ambo":
            return "Congratulations, it's a winning ticket!"
        elif len(check) >= 3 and self.bet.bet_type == "terno":
            return "Congratulations, it's a winning ticket!"
        elif len(check) >= 4 and self.bet.bet_type == "quaterna":
            return "Congratulations, it's a winning ticket!"
        elif len(check) >= 5 and self.bet.bet_type == "cinquina":
            return "Congratulations, it's a winning ticket!"
        else:
            return "Sorry, it's not a winning ticket.."    

#test
if __name__ == "__main__":
    board = ExtractionBoard
    ticket1 = Ticket("venezia", "  AmbaTa  ", 10)
    ticket2 = Ticket("RoMa ", "quAterNA", 7)
    ExtractionBoard.print_board(board)
    print()
    Ticket.print_ticket(ticket1)
    print(Ticket.set_win(ticket1))
    print()
    Ticket.print_ticket(ticket2)
    print(Ticket.set_win(ticket2))

