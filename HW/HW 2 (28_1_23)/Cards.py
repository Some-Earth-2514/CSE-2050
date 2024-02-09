import random


class Card:
    """Card class creates the Card objects"""

    def __init__(self, value, suit):
        """Initializes a new card with a value and suit"""
        self.value = value
        self.suit = suit

    def __repr__(self):
        """Returns the card's value and suit as a string"""
        return f"Card({self.value} of {self.suit})"

    def __lt__(self, other):
        """Returns the card which is < based on its suit(alphabetically) and value"""
        return (self.suit, self.value) < (other.suit, other.value)

    def __eq__(self, other):
        """Returns boolean value based on the fact if the card has same suit and value"""
        return (self.suit, self.value) == (other.suit, other.value)


class Deck:
    """Deck class creates the collection of all cards to make a deck"""
    def __init__(self, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                 suits=['clubs', 'diamonds', 'hearts', 'spades'], card_list=[]):
        """Initializes a deck based on a collection of values and suits from the cards"""
        self.values = values
        self.suits = suits
        self.card_list = []
        for value in self.values:
            for suit in self.suits:
                self.card_list.append(Card(value, suit))

    def __len__(self):
        """Returns the number of cards in a deck """
        return len(self.card_list)

    def sort(self):
        """Returns a sorted deck of cards(in order)"""
        return self.card_list.sort()

    def __repr__(self):
        """Returns a deck as a string"""
        return f"Deck: {self.card_list}"

    def shuffle(self):
        """Returns a shuffled order of the deck """
        return random.shuffle(self.card_list)

    def draw_top(self):
        """Returns the top card of the deck"""
        if len(self.card_list) == 0:
            raise RuntimeError("Cannot draw from empty deck")
        else:
            return self.card_list.pop()


class Hand(Deck):
    """Hand class creates the collection of all cards to make a hand"""

    def __init__(self, card_list=[]):
        """Initializes a collection of cards in hand"""
        super().__init__(card_list)
        self.card_list = card_list

    def __repr__(self):
        """Returns the hand as a string"""
        return f"Hand: {self.card_list}"

    def play(self, card):
        """Returns card from hand"""
        self.card = card
        if self.card in self.card_list:
            self.card_list.remove(self.card)
            return self.card
        else:
            raise RuntimeError(f"Attempt to play {self.card} that is not in Hand: {self.card_list}")
