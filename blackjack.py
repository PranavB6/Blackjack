from assests.Card import Card
from assests.Players import *
from random import shuffle
import queue

def main():

    cards = createCards()
    player = Player(cards)
    computer = Computer(cards)

    player.peak()
    computer.peak()

    pot = player.bet()
    pot += computer.bet(pot)

    player.peak()
    computer.peak()

    
    return

def createCards():

    cards = []
    suits = ['hearts', 'spades', 'diamonds', 'clubs']

    for suit in suits:
            
        for i in range(1, 11):
            cards.append(Card(str(i), suit, i))

        cards.append(Card('J', suit, 10))
        cards.append(Card('Q', suit, 10))
        cards.append(Card('K', suit, 10))

    shuffle(cards)

    card_queue = queue.Queue()

    for card in cards:               
        card_queue.put(card)

    return card_queue


if __name__ == "__main__": main()