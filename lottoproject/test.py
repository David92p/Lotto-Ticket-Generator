from ticket import Ticket
from header import Header

import argparse


def start(n):
    for i in range(n):
        ticket = Ticket()
        print()
        Header.horizontal()
        Header.vertical()
        Header.horizontal()
        Ticket.define_ticket(ticket)
        print()
    print("Good Luck")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lotto Ticket Generator")
    parser.add_argument("-n", "-number", type=int, help="Enter the number of tickets to be generated", choices=[0, 1, 2, 3, 4, 5])
    args = parser.parse_args()

    ticket = args.n
    # print(ticket)

    if ticket is None:
        print()
        print("""You can play 1 to 5 tickets. \nPress 0 if you want to exit the program""")
        print()

        while True:
            ticket = int(input("Enter the ticket number to play: "))
            if 0 < ticket <= 5:
                break
            elif ticket == 0:
                quit()
            else:
                print("You entered an invalid value")

    start(ticket)

