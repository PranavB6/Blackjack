

class Card:

    def __init__(self, surface, suit, value):

        self.surface = surface
        self.suit = suit
        self.value = value

    
    def __str__(self):
        return "Surface: {}, Suit: {}, Value: {}".format(self.surface, self.suit, self.value)