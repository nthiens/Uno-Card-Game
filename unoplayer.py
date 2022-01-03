from unodeck import *
from unocard import *


class Unoplayer:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hand = i.draw_initial()


    def show_hand(self):
        for o in self.hand:
            current_card = Card(o)
            current_card.show_card()

    def draw_from_pile(self):
        self.hand = self.hand + i.draw_one()

    def hand_points(self):
        pts = 0
        for card in self.hand:
            x = Card(card)
            pts = pts + x.card_points()
        return pts

    def in_hand(self, card_to_play):
        item = self.hand
        counter = 0
        while counter != len(item):
            if item[counter] == card_to_play:
                return True
            else:
                counter = counter + 1
        return False

    def play_color(self, cur_card, next_card):
        if cur_card.color == next_card[0]:
            self.hand.remove(next_card)
            return True
        return False

    def play_num(self, cur_card2, next_card2):
        if cur_card2.value == next_card2[1]:
            self.hand.remove(next_card2)
            return True
        return False

    def play_skip_reverse(self, cur_card3, next_card3):
        if cur_card3.color == next_card3[0]:
            self.hand.remove(next_card3)
            return True
        elif cur_card3.value == next_card3[1]:
            self.hand.remove(next_card3)
            return True
        else:
            return False

    def play_draw_2(self, cur_card4, next_card4):
        if cur_card4.color == next_card4[0]:
            self.hand.remove(next_card4)
            return True
        else:
            return False

    def play_choose(self, next_card5):
        self.hand.remove(next_card5)
        return True

    def play_draw_four(self, next_card6):
        self.hand.remove(next_card6)
        return True

    def usable_cards(self, cur_card_5):
        u_cards = []
        for c in self.hand:
            if c[0] == cur_card_5.color:
                u_cards = u_cards + [c]
            elif c[1] == cur_card_5.value:
                u_cards = u_cards + [c]
            elif (c[1] == "C") or (c[1] == "D"):
                u_cards = u_cards + [c]
        return u_cards
