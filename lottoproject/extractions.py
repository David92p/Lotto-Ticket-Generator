from .city import City

from random import sample

class ExtractionBoard:
    extractions = dict()

    for city in City.cities:
        extractions[city] = sample(list(range(1,90+1)),5) 

    def __init__(self):
        self.extractions = ExtractionBoard.extractions

    def print_board(self):
        title = "LOTTO TICKET"
        horizontal = '+' + '-' * 40 + '+'
        in_line = "+" + " " * 40 + "+"
        print(horizontal)
        print("|", title.center(38, " "), "|")
        print(horizontal)
        for bet, numbers in self.extractions.items():
            n = []
            for number in numbers:
                n.append(str(number))
            print("|", bet.center(10," "), "|", " ".join(n).center(25, " "), "|")
            print("|" + " " *12 + "|" + " "*27 + "|")
        print(horizontal)


#test
if __name__ == "__main__":
    board = ExtractionBoard()
    ExtractionBoard.print_board(board)