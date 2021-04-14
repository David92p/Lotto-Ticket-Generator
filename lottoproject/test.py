from ticket import Ticket

import argparse


def start(n):
    tickets = dict()
    for key in range(n):
        tickets[key] = Ticket()

    count_ticket = 1
    for key, values in tickets.items():
        print(f"Ticket Number {count_ticket}")
        Ticket.define_ticket(values)
        print()
        count_ticket += 1
    print()
    print("---------> Good Luck <---------")
    print()


parser = argparse.ArgumentParser(description="Welcome to Lotto Ticket Generator")
parser.add_argument("n", type=int, help="Enter the number of tickets to be generated", choices=[1,2,3,4,5])
args = parser.parse_args()

#test
if __name__ == "__main__":
    start(args.n)
