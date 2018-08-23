class Player:   

    def __init__(self, cards):
        self.money = 100
        self.cards = cards
        self.hand = []
        self.name = "Player"

        self.hit()
        self.hit()

    def points(self):
        points = 0
        for card in self.hand: points += card.value

        return points

    def hit(self):
        self.hand.append(self.cards.get())

    def bet(self):
        amount = int(input("Bet amount: "))
        self.money -= amount
        return amount

    def spill(self):
        print("========== {} ==========".format(self.name))
        print("Money: {}".format(self.money))
        print("Points: {}".format(self.points()))
        for card in self.hand: print(card)
        print()

    
    def peak(self):

        print(self.name, end = ": ")
        for card in self.hand:
            print("{} of {}, ".format(card.surface, card.suit), end = " ")

        print()

class Computer(Player):

    def __init__(self, cards):
        super().__init__(cards)
        self.name = "Computer"


    def bet(self, amount):
        self.money -= amount
        return amount