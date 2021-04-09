from game import Lotto
from header import Header


#The following class inherits from the Lotto class the necessary instances to be inserted into a table
class Ticket(Lotto):
    def __init__(self, city="", form="", numbers=""):
        super().__init__(city, form, numbers)

    def define_ticket(self):
        print("|", end="")
        for space in range(10):
            print(end=" ")
        print("|", end="")
        for space in range(24):
            print(end=" ")
        print("|")
        print("|", end="  ")
        print("CITY:   ", end="")
        print("|", end="")
        print(self.bet_city.center(23, " "), end=" ")
        print("|")
        print("|", end="")
        for space in range(10):
            print(end=" ")
        print("|", end="")
        for space in range(24):
            print(end=" ")
        print("|")
        print("|", end="  ")
        print("BET:    ", end="")
        print("|", end="")
        print(self.bet_form.center(23, " "), end=" ")
        print("|")
        print("|", end="")
        for space in range(10):
            print(end=" ")
        print("|", end="")
        for space in range(24):
            print(end=" ")
        print("|")
        print("|", end=" ")
        print("NUMBERS: ", end="")
        print("|", end="")
        if len(self.bet_numbers) <= 5:
            n = ""
            for i in range(len(self.bet_numbers)):
                n += str(self.bet_numbers[i])
                n += " "
            print(n.center(24, " "), end="")
            print("|")
            print("|", end="")
            for space in range(10):
                print(end=" ")
            print("|", end="")
            for space in range(24):
                print(end=" ")
            print("|")
        elif len(self.bet_numbers) > 5:
            n = ""
            for i in range(5):
                n += str(self.bet_numbers[i])
                n += " "
            print(n.center(23, " "), end=" ")
            print("|")
            print("|", end="")
            for space in range(10):
                print(end=" ")
            print("|", end="")
            n2 = ""
            for i in range(5, len(self.bet_numbers)):
                n2 += str(self.bet_numbers[i])
                n2 += " "
            print(n2.center(23, " "), end=" ")
            print("|")
        print("#", end="")
        for character in range(35):
            print("*", end="")
        print("#")

if __name__ == "__main__":
    ticket = Ticket()
    Header.horizontal()
    Header.vertical()
    Header.horizontal()
    Ticket.define_ticket(ticket)

