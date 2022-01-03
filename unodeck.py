import random

red_cards = (["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "RS", "RR", "Rd"] * 2) + ["R0"]
yellow_cards = (["Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "YS", "YR", "Yd"] * 2) + ["Y0"]
green_cards = (["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "GS", "GR", "Gd"] * 2) + ["G0"]
blue_cards = (["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "BS", "BR", "Bd"] * 2) + ["B0"]
special_cards = ["XC", "XC", "XC", "XC", "XD", "XD", "XD", "XD"]

all_cards = red_cards + yellow_cards + green_cards + blue_cards + special_cards
random.shuffle(all_cards)

red_cards_init = (["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9"] * 2) + ["R0"]
yellow_cards_init = (["Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9"] * 2) + ["Y0"]
green_cards_init = (["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9"] * 2) + ["G0"]
blue_cards_init = (["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"] * 2) + ["B0"]
all_cards_init = red_cards_init + yellow_cards_init + green_cards_init + blue_cards_init
random.shuffle(all_cards_init)

class Unodeck:

    def __init__(self, cards):
        self.cards = cards
        self.size = len(cards)

    def draw_one(self):
        one = [self.cards[0]]
        self.cards = self.cards[1:]
        self.size = self.size - 1
        return one

    def draw_two(self):
        two = [self.cards[0]] + [self.cards[1]]
        self.cards = self.cards[2:]
        self.size = self.size - 2
        return two

    def draw_four(self):
        four = [self.cards[0]] + [self.cards[1]] + [self.cards[2]] + [self.cards[3]]
        self.cards = self.cards[4:]
        self.size = self.size - 4
        return four

    def draw_initial(self):
        seven = [self.cards[0]] + [self.cards[1]] + [self.cards[2]] + [self.cards[3]] + [self.cards[4]] + \
                [self.cards[5]] + [self.cards[6]]
        self.cards = self.cards[7:]
        self.size = self.size - 7
        return seven


i = Unodeck(all_cards)

