class Card:
    # create a list for card face from 1~13 (its value)
    face = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # create a list for card suit ,Clubs=C, Diamonds=D, Spades=S, Hearts=H
    suit = ["C", "D", "S", "H"]

    def __init__(self, card_face: str = None, card_suit: str = None):
        self.card_face = int(card_face)
        self.card_suit = card_suit

    # visulaize the suit and unify tens digit to one character
    def __repr__(self):
        suitlist = {"C": "♣️", "D": "♦️", "S": "♠️", "H": "♥️"}
        facedic = {**{f: str(f) for f in range(2, 11)}, **{1: "A", 10: "T", 11: "J", 12: "Q", 13: "K"}}
        # print(self.card_face, self.card_suit)
        return facedic[self.card_face] + suitlist[self.card_suit]

    def set_card_face(self, card_face: int):
        self.card_face = card_face

    def set_card_suit(self, card_suit: str):
        self.card_suit = card_suit

    def get_card_face(self):
        return self.card_face

    def get_card_suit(self):
        return self.card_suit


def main():
    a = int(input("Please input the values of card face(1~13):"))
    b = input("Please input the suit of card (Clubs=C, Diamonds=D, Spades=S, Hearts=H):")
    while a not in Card.face or b not in Card.suit:
        print("Out of card range. Please check again.")
        a = int(input("Please input the values of card face(1~13):"))
        b = input("Please input the suit of card (Clubs=C, Diamonds=D, Spades=S, Hearts=H):")

    test = Card(a, b)
    print(test)


if __name__ == "__main__":
    main()
