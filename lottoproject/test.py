from lotto import Lotto

import argparse


def start(n):
    tickets = []
    for i in range(n):
        tickets.append(Lotto())
  
    for i, ticket in enumerate(tickets, 1):
        print(f"Ticket Number {i}")
        Lotto.print_ticket(ticket)
        print()
    print()
    print("---------> Good Luck <---------")
    print()


parser = argparse.ArgumentParser(description="Welcome to Lotto Ticket Generator")
parser.add_argument("n", type=int, help="Enter the number of tickets to be generated", choices=[1,2,3,4,5])
args = parser.parse_args()

#test
if __name__ == "__main__":
    start(args.n)
