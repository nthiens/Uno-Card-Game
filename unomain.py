from unodeck import *
from unoplayer import *
import random

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
colors = ["R", "B", "G", "Y"]

print(" __          ________ _      _____ ____  __  __ ______  ")
print(" \ \        / /  ____| |    / ____/ __ \|  \/  |  ____| ")
print("  \ \  /\  / /| |__  | |   | |   | |  | | \  / | |__    ")
print("   \ \/  \/ / |  __| | |   | |   | |  | | |\/| |  __|   ")
print("    \  /\  /  | |____| |___| |___| |__| | |  | | |____  ")
print("  ___\/__\/___|______|______\_____\____/|_|  |_|______| ")
print(" |__   __/ __ \                                         ")
print("    | | | |  | |                                        ")
print("    | | | |  | |                                        ")
print("    | | | |__| |                                        ")
print("  _ |_|_ \____/ ____                                    ")
print(" | |  | | \ | |/ __ \                                   ")
print(" | |  | |  \| | |  | |                                  ")
print(" | |  | | . ` | |  | |                                  ")
print(" | |__| | |\  | |__| |                                  ")
print("  \____/|_| \_|\____/                                   ")

deck_of_cards = Unodeck(all_cards)
cur_card = Card(all_cards_init[0])
your_name = input("\nWhat is your name? ")
print(f"\nWelcome {your_name}, you will be playing against a computer.")
print("------------------------------------------------------")
print("\nThe first card from the deck is drawn: ")
cur_card.show_card()
print("------------------------------------------------------")



state1 = True
state2 = True
player1 = Unoplayer(your_name)
player2 = Unoplayer("Computer")
game_over = False
winner = False
run_cpu = True
state3 = True

while game_over == False:
    while state1:
        if len(player1.hand) == 0 and winner == False:
            print(f"{player1.name} Wins!")
            print(f"The score is: {player2.hand_points()}")
            game_over = True
            winner = True
            state2 = False
            state3 = False
            break
        print(f"\n{your_name}, place a card from your hand:")
        player1.show_hand()
        play_move = input("I want to play: ")
        orig = play_move
        play1 = play_move + "ab"
        if orig == "pass":
            play = "pass"
        else:
            play = play1[0:2]
        if player1.in_hand(play) and play[1].isnumeric() and player1.play_color(cur_card, play):
            print("------------------------------------------------------")
            print("\nThe new card is: ")
            cur_card = Card(play)
            cur_card.show_card()
            state1 = False
            print("------------------------------------------------------")
        elif player1.in_hand(play) and play[1].isnumeric() and player1.play_num(cur_card, play):
            print("------------------------------------------------------")
            print("\nThe new card is: ")
            cur_card = Card(play)
            cur_card.show_card()
            state1 = False
            print("------------------------------------------------------")
        elif ((play[1] == "R") or (play[1] == "S")) and player1.in_hand(play) and player1.play_skip_reverse(cur_card,
                                                                                                            play):
            if play[1] == "R":
                print("------------------------------------------------------")
                print(f"You have skipped {player2.name}'s turn!\nPlay another card or type in 'pass' to draw a card.")
                print("\nThe new card is: ")
                cur_card = Card(play)
                cur_card.show_card()
                print("------------------------------------------------------")
            elif play[1] == "S":
                print("------------------------------------------------------")
                print(f"You have skipped {player2.name}'s turn!\nPlay another card or type in 'pass' to draw a card.")
                print("\nThe new card is: ")
                cur_card = Card(play)
                cur_card.show_card()
                print("------------------------------------------------------")
        elif (play[1] == "d") and (player1.in_hand(play)) and player1.play_draw_2(cur_card, play):
            print("------------------------------------------------------")
            print(f"{player2.name} has to draw two cards!")
            draw_two_cards = deck_of_cards.draw_two()
            player2.hand = player2.hand + draw_two_cards
            print("\nThe new card is: ")
            cur_card_color = play[0]
            random.shuffle(numbers)
            num2 = numbers[0]
            cur_card_value = str(num2)
            cur_card_total = cur_card_color + cur_card_value
            cur_card = Card(cur_card_total)
            cur_card.show_card()
            state1 = False
            print("------------------------------------------------------")
        elif (play[1] == "C") and (player1.in_hand(play)) and player1.play_choose(play):
            print("Choose a color: ")
            cur_color = "black"
            while True:
                col = input("Type in 'red', 'blue', 'green',or 'yellow': ")
                if (col == 'red') or (col == 'blue') or (col == 'green') or (col == 'yellow'):
                    cur_color = (col[0]).upper()
                    break
                else:
                    print("Invalid color! Try another color: ")
                    print("Choose one of the following: \n")

            print("------------------------------------------------------")
            print("\nThe new card is: ")
            cur_card_color = cur_color
            random.shuffle(numbers)
            num2 = numbers[0]
            cur_card_value = str(num2)
            cur_card_total = cur_card_color + cur_card_value
            cur_card = Card(cur_card_total)
            cur_card.show_card()
            state1 = False
            print("------------------------------------------------------")
        elif (play[1] == "D") and (player1.in_hand(play)) and player1.play_draw_four(play):
            print(f"{player2.name} has to draw four cards!\n")
            draw_four_cards = deck_of_cards.draw_four()
            player2.hand = player2.hand + draw_four_cards
            print("Choose a color: ")
            cur_color = "black"
            while True:
                col = input("Type in 'red', 'blue', 'green',or 'yellow': ")
                if (col == 'red') or (col == 'blue') or (col == 'green') or (col == 'yellow'):
                    cur_color = (col[0]).upper()
                    break
                else:
                    print("\nInvalid color! Try another color: ")
                    print("Choose one of the following: \n")
            print("------------------------------------------------------")
            print("\nThe new card is: ")
            cur_card_color = cur_color
            random.shuffle(numbers)
            num2 = numbers[0]
            cur_card_value = str(num2)
            cur_card_total = cur_card_color + cur_card_value
            cur_card = Card(cur_card_total)
            cur_card.show_card()
            state1 = False
            print("------------------------------------------------------")
        elif play == "pass":
            player1.draw_from_pile()
            state1 = False
        else:
            print("\nYou do not have this card on hand!\nChoose another card or type in 'pass' to draw a card.")
            print("\nThe current card is: ")
            cur_card.show_card()
        if len(player1.hand) == 0 and winner == False:
            print(f"{player1.name} Wins!")
            print(f"The score is: {player2.hand_points()}")
            game_over = True
            winner = True
            state2 = False
            state3 = False
            break

    if winner == True:
        state2 = False
    else:
        state2 = True

    while state2 and state3:
        if len(player2.hand) == 0 and winner == False:
            print(f"{player2.name} Wins!")
            print(f"The score is: {player1.hand_points()}")
            game_over = True
            winner = True
            state2 = False
            break
        elif len(player1.hand) == 0 and winner == True:
            print(f"{player1.name} Wins!")
            print(f"The score is: {player2.hand_points()}")
            game_over = True
            winner = True
            state2 = False
            break
        uc_deck = player2.usable_cards(cur_card)
        if uc_deck == []:
            uc_deck = ["pass"]
        random.shuffle(uc_deck)
        uc = uc_deck[0]
        print("------------------------------------------------------")
        print(f"\n{player2.name} chose to play: ")


        if uc == "pass":
            print("pass")
            print("and drew from the pile...")
            print("The current card is: ")
            cur_card.show_card()
            player2.draw_from_pile()
            state2 = False
            state1 = True
            print("------------------------------------------------------")
        elif uc[1].isnumeric() and player2.play_color(cur_card, uc):
            cur_card = Card(uc)
            cur_card.show_card()
            state2 = False
            state1 = True
            print("------------------------------------------------------")
        elif uc[1].isnumeric() and player2.play_num(cur_card, uc):
            cur_card = Card(uc)
            cur_card.show_card()
            state2 = False
            state1 = True
            print("------------------------------------------------------")
        elif ((uc[1] == "R") or (uc[1] == "S")) and player2.play_skip_reverse(cur_card, uc):
            if uc[1] == "R":
                print(f"\nYou have skipped {player1.name}'s turn!\nPlay another card or type in 'pass' to draw a card.")
                cur_card = Card(uc)
                cur_card.show_card()
                state1 = True
                print("------------------------------------------------------")
            elif uc[1] == "S":
                print(f"\nYou have skipped {player1.name}'s turn!\nPlay another card or type in 'pass' to draw a card.")
                cur_card = Card(uc)
                cur_card.show_card()
                state1 = True
                print("------------------------------------------------------")
        elif (uc[1] == "d") and (player2.in_hand(uc)) and player2.play_draw_2(cur_card, uc):
            print("Draw two cards!")
            print("\nThe current card is: ")
            draw_two_cards = deck_of_cards.draw_two()
            player1.hand = player1.hand + draw_two_cards
            cur_card_color = uc[0]
            random.shuffle(numbers)
            num2 = numbers[0]
            cur_card_value = str(num2)
            cur_card_total = cur_card_color + cur_card_value
            cur_card = Card(cur_card_total)
            cur_card.show_card()
            state2 = False
            state1 = True
            print("------------------------------------------------------")
        elif (uc[1] == "C") and (player2.in_hand(uc)) and player2.play_choose(uc):
            random.shuffle(colors)
            cur_color = colors[0]
            cur_card_color = cur_color
            random.shuffle(numbers)
            num2 = numbers[0]
            cur_card_value = str(num2)
            cur_card_total = cur_card_color + cur_card_value
            print("change color")
            cur_card = Card(cur_card_total)
            cur_card.show_card()
            state2 = False
            state1 = True
            print("------------------------------------------------------")
        elif (uc[1] == "D") and (player2.in_hand(uc)) and player2.play_draw_four(uc):
            print("Draw four cards!\n")
            print("The current card is: ")
            draw_four_cards = deck_of_cards.draw_four()
            player1.hand = player1.hand + draw_four_cards
            random.shuffle(colors)
            cur_color = colors[0]
            cur_card_color = cur_color
            random.shuffle(numbers)
            num2 = numbers[0]
            cur_card_value = str(num2)
            cur_card_total = cur_card_color + cur_card_value
            cur_card = Card(cur_card_total)
            cur_card.show_card()
            state2 = False
            state1 = True
            print("------------------------------------------------------")
        else:
            print("pass")
            player2.draw_from_pile()
            state2 = False
            state1 = True
            print("------------------------------------------------------")
        if len(player2.hand) == 0 and winner == False:
            print(f"{player2.name} Wins!")
            print(f"The score is: {player1.hand_points()}")
            game_over = True
            winner = True
            state2 = False
            break
