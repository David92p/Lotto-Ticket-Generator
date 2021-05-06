from lottoproject.lotto import Lotto
from lottoproject.ticket import Ticket

import argparse


def start(n):
    lotto = Lotto(n)
    for i, ticket in enumerate(lotto.tickets, 1):
        print()
        print(f"Ticket Number {i}")
        Ticket.print_ticket(ticket)
        print()
    print()
    print("---------> Good Luck <---------")
    print()




parser = argparse.ArgumentParser(description="Welcome to Lotto Ticket Generator")
parser.add_argument("-n", type=int, help="Enter the number of tickets to be generated", choices=[1,2,3,4,5])
args = parser.parse_args()

#test
if __name__ == "__main__":
    start(args.n)
