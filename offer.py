from dataclasses import dataclass

#Keeping Offer in an non changeable dataclass
@dataclass(frozen=True)
class Offer():
    quantity: int
    price: int
