from random import randrange
from tkinter import *
from tkinter import ttk
from tkinter import Tk
from tkinter.messagebox import showinfo

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
            Image.open("{}{}_of_{}.png".format(
                self.card_image_path,
                self.number_name_mapping.get(self.number, self.number),
                self.suit
            )).resize((103, 150),  Image.ANTIALIAS)
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

        except IndexError or ValueError:
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

    def draw_card(self):
        card = self.deck.give_random_card()
        self.table_cards.append(card)
        return card

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

    def calculate_player_score(self):
        return self._calculate_score(self.player.get_player_card())

    def calculate_dealer_score(self):
        return self._calculate_score(self.dealer.get_player_card())

    def does_player_wins(self):
        player_score = self.calculate_player_score()
        dealer_score = self.calculate_dealer_score()

        if player_score > 21:
            return False
        elif player_score > dealer_score:
            return True
        elif dealer_score > 21:
            return True
        else:
            return False


class BlackjackUI:
    back_card_img_path = "./asset/png/back.png"

    def __init__(self):
        self.ui_root = Tk()

        self.ui_title_frame = ttk.Frame(self.ui_root, padding="30 12 30 12")
        self.ui_title_frame.grid(sticky=(W, E))

        self.ui_table_frame = ttk.Frame(self.ui_root, padding="30 12 30 12", width=200, height=450)
        self.ui_table_frame.grid(sticky=(W, E))

        self.ui_table_frame.rowconfigure(1, minsize=150)
        self.ui_table_frame.rowconfigure(1, minsize=150)
        self.ui_table_frame.rowconfigure(1, minsize=150)

        self.ui_score_frame = ttk.Frame(self.ui_root, padding="30 12 30 12")
        self.ui_score_frame.grid(sticky=(W, E))

        ttk.Label(self.ui_title_frame, text="Blackjack", width=60).grid(column=1, row=1)
        ttk.Button(self.ui_title_frame, text="Play", command=self.start_game).grid(column=2, row=1)

        ttk.Label(self.ui_score_frame, text="Your points").grid(column=1, row=1)

        self.player_score_label = ttk.Label(self.ui_score_frame, text="0", width=12)
        self.player_score_label.grid(column=2, row=1)

        ttk.Label(self.ui_score_frame, text="Dealer points").grid(column=3, row=1)

        self.dealer_score_label = ttk.Label(self.ui_score_frame, text="???", width=12)
        self.dealer_score_label.grid(column=4, row=1)

        self.ui_give_card_button = ttk.Button(self.ui_score_frame, text="Draw",
                                              command=self.draw_card, state=DISABLED)
        self.ui_end_game_button = ttk.Button(self.ui_score_frame, text="Stay",
                                             command=self.end_game, state=DISABLED)

        self.ui_give_card_button.grid(column=5, row=1)
        self.ui_end_game_button.grid(column=6, row=1)

        self.game = None
        self.dealer_card = None
        self.ui_player_card_label = None
        self.ui_dealer_card_label = None
        self.ui_empty_table_label = None

        self.tk_back_card_img = ImageTk.PhotoImage(
            Image.open(self.back_card_img_path).resize((103, 150),  Image.ANTIALIAS))

    def end_game(self):
        dealer_score = self.game.calculate_dealer_score()

        self.dealer_score_label.config(text=dealer_score)
        self.ui_dealer_card_label.config(image=self.dealer_card.tk_img)

        if self.game.does_player_wins():
            showinfo('Match Results', 'You Win!')
        else:
            showinfo('Match Results', 'You Lose!')

        self.ui_give_card_button.config(state=DISABLED)
        self.ui_end_game_button.config(state=DISABLED)

    def start_game(self):
        self.game = Blackjack()
        self.dealer_score_label.config(text="???")
        player_card, self.dealer_card = self.game.give_initial_cards()

        self.ui_player_card_label = ttk.Label(self.ui_table_frame, image=player_card.tk_img)
        self.ui_player_card_label.grid(column=1, row=3)

        self.ui_empty_table_label = ttk.Label(self.ui_table_frame, padding="12 30 12 30")
        self.ui_empty_table_label.grid(column=1, row=2)

        self.ui_dealer_card_label = ttk.Label(self.ui_table_frame, image=self.tk_back_card_img)
        self.ui_dealer_card_label.grid(column=1, row=1)

        self.draw_card()

        self.ui_give_card_button.config(state=ACTIVE)
        self.ui_end_game_button.config(state=ACTIVE)

    def draw_card(self):
        card = self.game.draw_card()
        card_label = ttk.Label(self.ui_table_frame, image=card.tk_img)
        card_label.grid(column=self.game.get_table_cards_counts() + 1, row=3)

        player_score = self.game.calculate_player_score()
        self.player_score_label.config(text=player_score)

        if player_score > 21:
            self.end_game()

    def run(self):
        self.ui_root.mainloop()


if __name__ == '__main__':
    BlackjackUI().run()
