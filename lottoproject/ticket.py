from city import City
from bet import TicketType

from random import sample

class Ticket:
    def __init__(self, city, bet, quantity_numbers):
        self.city = City(city)
        self.bet = TicketType(bet)
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
        print("|",self.city.bet_city.upper().center(38, " "),"|")
        print(in_line)
        print("|",self.bet.bet_type.upper().center(38, " "),"|")
        print(in_line)
        print("|"," ".join(self.numbers).center(38, " "),"|")
        print(in_line)
        print(horizontal)
        

   

#test
if __name__ == "__main__":
    ticket1 = Ticket("Milano", "  AmbaTa  ", 3)
    ticket2 = Ticket("RoMa ", "quAterNA", 10)
    Ticket.print_ticket(ticket1)
    print()
    Ticket.print_ticket(ticket2)
