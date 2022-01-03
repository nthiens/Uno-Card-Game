class color:
    PURPLE = '\033[95m'
    BLACK = '\033[30m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


"""
R - Red
Y - Yellow
G - Green
B - Blue
X - Any

0
1
2
:
:
9
d - Draw 2
D - Draw 4
R - Reverse
S - Skip
C - Choose Color
"""


class Card:
    dictionary = {"0": "Zero", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five",
                  "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine", "d": "Draw 2 Cards", "D": "Draw 4 Cards",
                  "R": "Reverse", "S": "Skip", "C": "Choose Color"}

    def __init__(self, uno_card):
        self.color = uno_card[0]
        self.value = uno_card[1]
        self.symbol = Card.dictionary[self.value]

    def card_points(self):
        if self.value.isnumeric():
            return int(self.value)
        elif self.value == "d" or self.value == "R" or self.value == "S":
            return 20
        else:
            return 50

    def show_card(self):
        if self.color == "R":
            print(color.RED + ".------." + color.END)
            if self.value.isnumeric():
                print(color.RED + "|" + color.END + self.value + color.RED + ".--. |" + color.END)
            elif self.value == "S":
                print(color.RED + "|" + color.END + "Ø" + color.RED + ".--. |" + color.END)
            elif self.value == "R":
                print(color.RED + "|" + color.END + "→" + color.RED + ".--. |" + color.END)
            elif self.value == "d":
                print(color.RED + "|" + color.END + "+2" + color.RED + "--. |" + color.END)
            print(color.RED + "| :/\: |" + color.END + "       Card Name:")
            print(color.RED + "| :\/: |" + color.END + "       " + self.color + self.value + ", Red " + self.symbol)
            if self.value.isnumeric():
                print(color.RED + "| '--'" + color.END + self.value + color.RED + "|" + color.END)
            elif self.value == "S":
                print(color.RED + "| '--'" + color.END + "Ø" + color.RED + "|" + color.END)
            elif self.value == "R":
                print(color.RED + "| '--'" + color.END + "←" + color.RED + "|" + color.END)
            elif self.value == "d":
                print(color.RED + "| '--" + color.END + "+2" + color.RED + "|" + color.END)
            print(color.RED + "`------'" + color.END)
        elif self.color == "Y":
            print(color.YELLOW + ".------." + color.END)
            if self.value.isnumeric():
                print(color.YELLOW + "|" + color.END + self.value + color.YELLOW + ".--. |" + color.END)
            elif self.value == "S":
                print(color.YELLOW + "|" + color.END + "Ø" + color.YELLOW + ".--. |" + color.END)
            elif self.value == "R":
                print(color.YELLOW + "|" + color.END + "→" + color.YELLOW + ".--. |" + color.END)
            elif self.value == "d":
                print(color.YELLOW + "|" + color.END + "+2" + color.YELLOW + "--. |" + color.END)
            print(color.YELLOW + "| :/\: |" + color.END + "       Card Name:")
            print(color.YELLOW + "| :\/: |" + color.END + "       " + self.color + self.value + ", Yellow " + self.symbol)
            if self.value.isnumeric():
                print(color.YELLOW + "| '--'" + color.END + self.value + color.YELLOW + "|" + color.END)
            elif self.value == "S":
                print(color.YELLOW + "| '--'" + color.END + "Ø" + color.YELLOW + "|" + color.END)
            elif self.value == "R":
                print(color.YELLOW + "| '--'" + color.END + "←" + color.YELLOW + "|" + color.END)
            elif self.value == "d":
                print(color.YELLOW + "| '--" + color.END + "+2" + color.YELLOW + "|" + color.END)
            print(color.YELLOW + "`------'" + color.END)
        elif self.color == "G":
            print(color.GREEN + ".------." + color.END)
            if self.value.isnumeric():
                print(color.GREEN + "|" + color.END + self.value + color.GREEN + ".--. |" + color.END)
            elif self.value == "S":
                print(color.GREEN + "|" + color.END + "Ø" + color.GREEN + ".--. |" + color.END)
            elif self.value == "R":
                print(color.GREEN + "|" + color.END + "→" + color.GREEN + ".--. |" + color.END)
            elif self.value == "d":
                print(color.GREEN + "|" + color.END + "+2" + color.GREEN + "--. |" + color.END)
            print(color.GREEN + "| :/\: |" + color.END + "       Card Name:")
            print(color.GREEN + "| :\/: |" + color.END + "       " + self.color + self.value + ", Green " + self.symbol)
            if self.value.isnumeric():
                print(color.GREEN + "| '--'" + color.END + self.value + color.GREEN + "|" + color.END)
            elif self.value == "S":
                print(color.GREEN + "| '--'" + color.END + "Ø" + color.GREEN + "|" + color.END)
            elif self.value == "R":
                print(color.GREEN + "| '--'" + color.END + "←" + color.GREEN + "|" + color.END)
            elif self.value == "d":
                print(color.GREEN + "| '--" + color.END + "+2" + color.GREEN + "|" + color.END)
            print(color.GREEN + "`------'" + color.END)
        elif self.color == "B":
            print(color.BLUE + ".------." + color.END)
            if self.value.isnumeric():
                print(color.BLUE + "|" + color.END + self.value + color.BLUE + ".--. |" + color.END)
            elif self.value == "S":
                print(color.BLUE + "|" + color.END + "Ø" + color.BLUE + ".--. |" + color.END)
            elif self.value == "R":
                print(color.BLUE + "|" + color.END + "→" + color.BLUE + ".--. |" + color.END)
            elif self.value == "d":
                print(color.BLUE + "|" + color.END + "+2" + color.BLUE + "--. |" + color.END)
            print(color.BLUE + "| :/\: |" + color.END + "       Card Name:")
            print(color.BLUE + "| :\/: |" + color.END + "       " + self.color + self.value + ", Blue " + self.symbol)
            if self.value.isnumeric():
                print(color.BLUE + "| '--'" + color.END + self.value + color.BLUE + "|" + color.END)
            elif self.value == "S":
                print(color.BLUE + "| '--'" + color.END + "Ø" + color.BLUE + "|" + color.END)
            elif self.value == "R":
                print(color.BLUE + "| '--'" + color.END + "←" + color.BLUE + "|" + color.END)
            elif self.value == "d":
                print(color.BLUE + "| '--" + color.END + "+2" + color.BLUE + "|" + color.END)
            print(color.BLUE + "`------'" + color.END)
        elif self.color == "X":
            print(color.BLACK + ".------." + color.END)
            if self.value == "C":
                print(color.BLACK + "|" + color.END + "◕" + color.BLACK + ".--. |" + color.END)
            elif self.value == "D":
                print(color.BLACK + "|" + color.END + "+4" + color.BLACK + "--. |" + color.END)
            print(color.BLACK + "| :/\: |" + color.END + "       Card Name:")
            print(color.BLACK + "| :\/: |" + color.END + "       " + self.color + self.value + ", Black " + self.symbol)
            if self.value == "C":
                print(color.BLACK + "| '--'" + color.END + "◕" + color.BLACK + "|" + color.END)
            elif self.value == "D":
                print(color.BLACK + "| '--" + color.END + "+4" + color.BLACK + "|" + color.END)
            print(color.BLACK + "`------'" + color.END)
