from abc import ABC, abstractmethod


class Wear(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Wear):
    def __init__(self, v):
        self.v = v

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5


class Suit(Wear):
    def __init__(self, h):
        self.h = h

    @property
    def consumption(self):
        return 2 * self.h + 0.3


coat = Coat(50)
print(coat.consumption)

suit = Suit(50)
print(suit.consumption)
