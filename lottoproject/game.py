from basic import BasicGame

from random import sample

#The following class, after inheriting a correct city and form, takes care of instantiating a list of numbers in the correct way
class Lotto(BasicGame):
    def __init__(self, city="", form="", numbers=""):
        super().__init__(city, form)
        self.bet_numbers = Lotto.set_numbers(self)

    #The function calls the form instance and returns the requested number instance correctly
    def set_numbers(self):
        print("""
            Enter the desired amount of numbers, remember to enter a minimum amount based on your stake up to a maximum of 10 numbers.
            Example:          --> "TERNO" MIN 3 NUMBERS MAX 10 NUMBERS <--
            """)
        while True:
            n = int(input("Enter the amount of numbers you want to play: "))
            if self.bet_form == "ambata" and 1 <= n <= 10:
                break
            elif self.bet_form == "ambo" and 2 <= n <= 10:
                break
            elif self.bet_form == "terno" and 3 <= n <= 10:
                break
            elif self.bet_form == "quaterna" and 4 <= n <= 10:
                break
            elif self.bet_form == "cinquina" and 5 <= n <= 10:
                break
            else:
                print("It is not possible to play this amount of numbers for the desired form of bet")

        self.bet_numbers = list(sample(range(1, 90 + 1), n))
        return self.bet_numbers

    def __str__(self):
        return f"{self.bet_city}, {self.bet_form}, {self.bet_numbers}"


# test
if __name__ == "__main__":
    ticket = Lotto()
    print(ticket)

