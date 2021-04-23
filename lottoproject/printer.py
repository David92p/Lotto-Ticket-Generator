#The following class inherits from the Lotto class the necessary instances to be inserted into a table
class Printed:
    max_horizontal_characters = 35
    title = "LOTTO TICKET"

    def __init__(self, form, city, numbers):
        self.form = form
        self.city = city
        self.numbers = numbers
    
    # The following method allows you to print our ticket header
    @staticmethod
    def header():
        print("#", end="")
        for character in range(Printed.max_horizontal_characters):
            print("*", end="")
        print("#")
        print("*", end="")
        print(Printed.title.center(35, " "), end="")
        print("*")
        print("#", end="")
        for character in range(Printed.max_horizontal_characters):
            print("*", end="")
        print("#")

    # The following method allows you to print the body of our ticket
    def body(self):
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
        print(self.city.center(23, " "), end=" ")
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
        print(self.form.center(23, " "), end=" ")
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
        if len(self.numbers) <= 5:
            n = ""
            for i in range(len(self.numbers)):
                n += str(self.numbers[i])
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
        elif len(self.numbers) > 5:
            n = ""
            for i in range(5):
                n += str(self.numbers[i])
                n += " "
            print(n.center(23, " "), end=" ")
            print("|")
            print("|", end="")
            for space in range(10):
                print(end=" ")
            print("|", end="")
            n2 = ""
            for i in range(5, len(self.numbers)):
                n2 += str(self.numbers[i])
                n2 += " "
            print(n2.center(23, " "), end=" ")
            print("|")
        print("#", end="")
        for character in range(35):
            print("*", end="")
        print("#")

if __name__ == "__main__":
    ticket = Printed.body()
    #Ticket.define_ticket(ticket)

