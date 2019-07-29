from random import randrange


class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit


class Deck:
    # need create: shuffle method
    suits = ["diamonds", "heart", "spades", "clubs"]
    max_number = 13

    def __int__(self):
        self.cards = []

        for suit in self.suits:
            for number in range(1, self.max_number):
                self.cards.append(Card(number, suit))

    def give_random_card(self):
        # move this method to BlackjackGame.
        try:
            cards_left = len(self.cards)
            return self.cards.pop(randrange(cards_left))
        except IndexError:
            print("There are no more cards in the deck")
            # shuffle method needed here


class Player:
    # Player need money
    def __int__(self, name, points):
        self.name = name
        self.points = points


class BlackjackGame:
    def __int__(self, player, deck):
        self.player = player
        self.deck = deck

    def player_turn:
        while palyer

    def who_wins(self):
        if player.points > 21:
            player_lose



# need a new class, croupier.

