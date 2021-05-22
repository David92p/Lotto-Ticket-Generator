from .city import City
from .bet import TicketType
from .ticket import Ticket

# Logic Class
class Lotto:
    def __init__(self, quantity_tickets):
        self.tickets = []
        Lotto.generate_ticket(self, quantity_tickets)
        
    # The following function takes care of carrying out a check on the parameters to pass to our list of Tickets
    def generate_ticket(self, quantity_tickets):
        for i in range(quantity_tickets):
            while True:
                try:
                    print("""
                    List of the Citys:

                        - Bari 
                        - Cagliari 
                        - Firenze 
                        - Genova 
                        - Milano 
                        - Napoli 
                        - Palermo 
                        - Roma 
                        - Torino 
                        - Venezia
                        
                        """ )
                    chosen_city = input("Enter the city for your bet: ")
                    chosen_city = chosen_city.strip().lower()
                    if City.check_cities(chosen_city):
                        city = chosen_city
                        break
                except ValueError:
                    print("City Non Valid")

            while True:
                try:
                    print("""
                    List of the Bets Types:
                        
                        - Ambata
                        - Ambo 
                        - Terno 
                        - Quaterna 
                        - Cinquina
                        
                        """)
                    chosen_bet = input("Enter the type for your bet: ")
                    chosen_bet = chosen_bet.strip().lower()
                    if TicketType.check_bet(chosen_bet):
                        bet = chosen_bet
                        break
                except ValueError:
                    print("Bet Non Valid")

            while True:
                try:
                    n = int(input("Enter the amount of numbers you want to play: "))
                    if bet == "ambata" and 1 <= n <= 10:
                        quantity_numbers = n
                        break
                    elif bet == "ambo" and 2 <= n <= 10:
                        quantity_numbers = n
                        break
                    elif bet == "terno" and 3 <= n <= 10:
                        quantity_numbers = n
                        break
                    elif bet == "quaterna" and 4 <= n <= 10:
                        quantity_numbers = n
                        break
                    elif bet == "cinquina" and 5 <= n <= 10:
                        quantity_numbers = n
                        break
                    else:
                        print("It is not possible to play this amount of numbers for the desired form of bet")
                except ValueError:
                    print("Enter a numeric value")
 
            self.tickets.append(Ticket(city, bet, quantity_numbers))
    
            


    
#test
if __name__ == "__main__":
    tickets = Lotto(2)
    
    