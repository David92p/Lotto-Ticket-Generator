from random import sample

class Numbers:
    def __init__(self, quantity_numbers):
        self.bet_numbers = Numbers.check_numbers(quantity_numbers)

    # The following function takes care of returning a series of numbers
    @staticmethod
    def check_numbers(quantity_numbers):
        numbers = ""
        list_numbers = list(sample(range(1, 90 + 1), quantity_numbers))
        for n in list_numbers:
            numbers += str(n) + " "
        return numbers

    def __str__(self):
        return self.bet_numbers

#test
if __name__== "__main__":
    n = Numbers(6)
    print(n)