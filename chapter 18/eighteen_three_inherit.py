import sys
import os
import random


class Card(object):
    all_suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    all_ranks = [None, 'Ace', '2', '3', '4', '5', '6', '7','8',
        '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=1):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{1} of {0}".format(Card.all_suits[self.suit], Card.all_ranks[self.rank])

    def __cmp__(self, other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        return 0


class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                localcard = Card(suit, rank)
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
        self.cards.sort(cmp=Card.__cmp__)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal(self, num_hands, cards_per_hand):
        for handcount in range(num_hands):
            hand_name = "hand" +str(handcount + 1)
            localhand = Hand(hand_name)
            self.move_cards(localhand, 3)
            print localhand

    def deal_hands(self, num_of_hands, cards_per_hand):
        for hand_count in range(num_of_hands):
            # Create hand and label based on index
            hand_name = 'hand_num' + str(hand_count)
            localhand = Hand(hand_name)
            print
            print "Created hand called", hand_name
            for card_count in range(cards_per_hand):
                # Pop cards into hand from the deck
                localhand.add_card(self.pop_card())
            print "Hand has cards"
            print localhand
            print "#" * 30


class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label
        
    def __str__(self):
        res = []
        for localcard in self.cards:
            res.append(localcard.__str__())
            #print localcard
        return self.label + "," + str(res)

    
def main():
    card1 = Card(2, 13)
    card2 = Card(2, 12)
    deck1 = Deck()
    hand1 = Hand("hand1")
    #deck1.move_cards(hand1,5)
    hand1.add_card(card1)
    hand1.add_card(card2)
    print hand1
    print deck1
    deck1.deal(3, 3)
    #deck1.deal_hands(3, 3)


if __name__ == "__main__":
    main()
