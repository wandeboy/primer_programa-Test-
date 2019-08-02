from random import randrange
from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image


class Player:
    def __init__(self):
        self._initial_cards = None

    def get_player_card(self):
        return self._initial_cards

    def set_player_card(self, initial_card):
        self._initial_cards = initial_card


class Card:
    number_name_mapping = {
        1: "ace",
        11: "jack",
        12: "queen",
        13: "king"
    }
    
    card_image_path = "./asset/png/"

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        self.tk_img = ImageTk.PhotoImage(
            Image.open("{}{}_of_{}".format(
                self.card_image_path,
                self.number_name_mapping.get(self.number, self.number),
                self.suit
            ))
        )


class Deck:
    suits = ["diamonds", "hearts", "spades", "clubs"]
    max_number = 13

    def __init__(self):
        self.cards = []
        self.used_cards = []

        for suit in self.suits:
            for number in range(1, self.max_number + 1):
                self.cards.append(Card(number, suit))

    def give_random_card(self):
        try:
            cards_left = len(self.cards)
            chosen_card = self.cards.pop(randrange(cards_left))
            self.used_cards.append(chosen_card)
            return chosen_card

        except IndexError:
            print("There are no more cards in the deck")
            # shuffle method needed here


class Blackjack:
    card_values = {
        1: 11,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 10,
        12: 10,
        13: 10
    }

    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Player()
        self.table_cards = []

    def give_initial_cards(self):
        player_card = self.deck.give_random_card()
        dealer_card = self.deck.give_random_card()
        self.player.set_player_card(player_card)
        self.dealer.set_player_card(dealer_card)
        return player_card, dealer_card

    def draft_card(self):
        card = self.deck.give_random_card()
        self.table_cards.append(card)
        return

    def _calculate_score(self, player_card):
        total = 0
        cards = [player_card]
        cards.extend(self.table_cards)
        for card in cards:
            if card.number == 1 and total + self.card_values[card.number] > 21:
                total += 1
            else:
                total += self.card_values[card.number]
        return total

    def get_table_cards_counts(self):
        return len(self.table_cards)


class BlackjackUI:
    def __init__(self):
        self.ui_root = Tk()

        self.ui_title_frame = ttk.Frame(self.ui_root, padding="30 12 30 12")
        self.ui_title_frame.grid(sticky=(W, E))

    def run(self):
        self.ui_root.mainloop()


if __name__ == '__main__':
    BlackjackUI().run()

