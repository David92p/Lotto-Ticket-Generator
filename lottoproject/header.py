# The following Class allows you to print the header of your ticket
class Header:
    max_horizontal_characters = 35
    title = "LOTTO TICKET"

    # The following method allows you to print the horizontal lines of your ticket
    @staticmethod
    def horizontal():
        print("#", end="")
        for character in range(Header.max_horizontal_characters):
            print("*", end="")
        print("#")

    # The following method allows you to print the vertical lines of the header of your ticket
    # Not reusable for the remainder of the ticket
    @staticmethod
    def vertical():
        print("*", end="")
        print(Header.title.center(35, " "), end="")
        print("*")


# test
if __name__ == "__main__":
    Header.horizontal()
    Header.vertical()
    Header.horizontal()
