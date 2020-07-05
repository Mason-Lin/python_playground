from dataclasses import dataclass
import attr

@dataclass
class Card():
    rank: str
    suit: str

card = Card('Q', "hearts")

print(card == card)
print(card.rank)

