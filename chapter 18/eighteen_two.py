import sys
import os
import random

class card(object):
    all_suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    all_ranks = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', 
        '9', '10', 'Jack', 'Queen', 'King']


    def __init__(self,suit=0 ,rank=1):
        self.suit = suit
        self.rank = rank



    def __str__(self):
        return "{1} of {0}".format(card.all_suits[self.suit], card.all_ranks[self.rank])

    def __cmp__(self, other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        return 0
    
class deck(object):

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                localcard = card(suit, rank)
                self.cards.append(localcard)

    def __str__(self):
        res = []
        for c in self.cards:
            res.append(str(c))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()
    def add_card(self, card):
        self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards)
    def sort(self):
        # Method to have deck sort itself.
        self.cards.sort(cmp=card.__cmp__)
        
card1 = card(2, 13)
card2 = card(2, 12)
deck1 = deck()
print card1,'and', card2
print card1 > card2

print "deck of cards created \n\n"
print deck1, '\n'
deck1.shuffle()
print "shffle \n"
print deck1, '\n'
deck1.sort()
print "sorted\n"
print deck1



