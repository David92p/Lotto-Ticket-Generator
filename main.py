from lottoproject.lotto import Lotto

import argparse

def start(n):
    lotto = Lotto(n)
    Lotto.printer(lotto)
    print()
    print("---------> Good Luck <---------")
    print()




parser = argparse.ArgumentParser(description="Welcome to Lotto Ticket Generator")
parser.add_argument("-n", type=int, help="Enter the number of tickets to be generated", choices=[1,2,3,4,5])
args = parser.parse_args()

#test
if __name__ == "__main__":
    start(args.n)