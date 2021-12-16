import random
from typing import List

from Card import Card


class Deck:
    def __init__(self, value_start=None, value_end=None, number_of_suit=None):
        assert 1 < number_of_suit <= 4, "number_of_suit must between 1~4"
        self.deck = []
        for suits in Card.suit[0:number_of_suit]:
            for faces in Card.face[(value_start - 1) : value_end]:
                self.deck += [Card(faces, suits)]

    def set_deck(self, value_start, value_end, number_of_suit):
        for suits in Card.suit[0:number_of_suit]:
            for faces in Card.face[(value_start - 1) : value_end]:
                self.deck += [Card(faces, suits)]

    def get_deck(self):
        return self.deck

    def display_deck(self):
        for i, card in enumerate(self.deck):
            if i % 8 == 0:
                print()
            print(f"{card} ", end="")
        print()

    def shuffle(self) -> List[Card]:
        random.shuffle(self.deck)

    def add_card(self, card: Card):
        self.deck.append(card)

    def draw_card(self) -> Card:
        return self.deck.pop()


def main():
    test_deck = Deck(1, 13, 4)
    test_deck.shuffle()
    test_deck.add_card(Card("2", "S"))
    test_deck.display_deck()
    print(test_deck.draw_card())


if __name__ == "__main__":
    main()
