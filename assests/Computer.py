class Computer:   

    def __init__(self, cards):
        self.money = 100
        self.cards = cards
        self.hand = []


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

    def peak(self):
        print("Money: {}".format(self.money))
        print("Points: {}".format(self.points()))

        print("-------------------------")
        for card in self.hand: print(card)