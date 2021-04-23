from city import City
from form import Form
from printer import Printed

from random import sample

# Logic Class
class Lotto:
    def __init__(self, city="", form="", numbers=""):
        self.city = City.check_cities()
        self.form = Form.check_form()
        self.numbers = Lotto.generator_numbers(self)

    # The function calls the form instance and returns the requested number instance correctly
    def generator_numbers(self):
        print("""
            Enter the desired amount of numbers, remember to enter a minimum amount based on your stake up to a maximum of 10 numbers.
            Example:          --> "TERNO" MIN 3 NUMBERS MAX 10 NUMBERS <--
            """)
        while True:
            n = int(input("Enter the amount of numbers you want to play: "))
            if self.form == "ambata" and 1 <= n <= 10:
                break
            elif self.form == "ambo" and 2 <= n <= 10:
                break
            elif self.form == "terno" and 3 <= n <= 10:
                break
            elif self.form == "quaterna" and 4 <= n <= 10:
                break
            elif self.form == "cinquina" and 5 <= n <= 10:
                break
            else:
                print("It is not possible to play this amount of numbers for the desired form of bet")

        self.numbers = list(sample(range(1, 90 + 1), n))
        return self.numbers

    def print_ticket(self):
        Printed.header()
        Printed.body(self)


    def __str__(self):
        return f"{self.city}, {self.form}, {self.numbers}"


# test
if __name__ == "__main__":
    ticket = Lotto()
    Lotto.print_ticket(ticket)

