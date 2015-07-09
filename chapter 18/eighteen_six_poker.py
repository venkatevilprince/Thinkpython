"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from eighteen_three_inherit import *


class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        print self.suits
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def rank_hist(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
            
    def has_pairs(self):

        self.rank_hist()
        #print self.ranks
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_two_pairs(self):

        self.rank_hist()
        #print self.ranks
        flag = 0
        for val in self.ranks.values():
            if val >= 2:
                flag += 1
                if flag >= 2:
                    return True
        return False

    def has_three_of_a_kind(self):
        self.suit_hist()
        for val in self.suits.values():
            if val > 3:
                return True
        return False

    def classify(self):
        self.priority = [(None,None)]
        if self.has_pairs():
            self.priority.append((1,"pair"))
        if self.has_two_pairs():
            self.priority.append((2,"two pair"))
        if self.has_three_of_a_kind():
            self.priority.append((3,"three of a kind"))        
        self.priority.sort(reverse=True)
        x, y = self.priority[0]
        if(y):
            self.label = y
        else:
            self.label = "None"
            

        
        
        

if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand("hand{}".format(i+1))
        deck.move_cards(hand, 7)
        hand.sort()
        hand.classify()
        print hand
        print ''
