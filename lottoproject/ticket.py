from city import City
from bet import TicketType
from numbers import Numbers

class Ticket:
    def __init__(self, city, bet, quantity_numbers):
        self.city = City(city)
        self.bet = TicketType(bet)
        self.numbers = Numbers(quantity_numbers)
        
    def print_ticket(self):
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
        print("|",self.numbers.bet_numbers.center(38, " "),"|")
        print(in_line)
        print(horizontal)
        

   

#test
if __name__ == "__main__":
    ticket1 = Ticket("Milano", "  AmbaTa  ", 3)
    ticket2 = Ticket("RoMa ", "quAterNA", 10)
    Ticket.print_ticket(ticket1)
    print()
    Ticket.print_ticket(ticket2)
