from random import shuffle
from card import *
import copy
class Set:

    def __init__(self, owner, deck=None):
        self.hand=[]
        if not deck:
            self.deck = self.make_deff_deck(owner)
        else:
            self.deck=deck
        self.all=copy.copy(self.deck)
        self.discard=[]
        self.pending=[]
        self.in_play=[]
        self.trash_list = []
        self.token_points=0
        self.shuffle_deck()

    def make_deff_deck(self, owner):
        start = [Copper(owner) for _ in range(7)]
        start.extend([Estate(owner) for _ in range(3)])
        return start



    def draw(self, num=1):
        for _ in range(num):
            self.hand.append(self.getTop())

    def getTop(self):
        if len(self.deck) > 0:
            return self.deck.pop()
        else:
            self.reshuffle_discard()
            return self.deck.pop()

    def reshuffle_discard(self):
        self.deck.extend(self.discard)
        self.discard=[]
        self.shuffle_deck()

    def shuffle_deck(self):
        shuffle(self.deck)


    def play_card(self, loc):
        card = self.hand.pop(loc)
        card.play()
        self.in_play.append(card)
        return card
        # card.play()

    def play(self, name):
        card_to_play = card_dict[name]
        for i,card in enumerate(self.hand):
            if type(card) is card_to_play:
                return self.play_card(i)


    def end_turn(self):
        self.discard.extend(self.hand)
        self.discard.extend(self.in_play)
        self.hand=[]
        self.in_play=[]
        self.draw(5)

    def gain(self,card):
        self.discard.append(card)
        self.all.append(card)

    def add_to_hand(self, card):
        self.hand.append(card)
        self.all.append(card)

    def trash(self, place, position):
        var = self.__dict__.get(place)
        if var and type(var) is list and var is not self.trash_list:
            card = var.pop(position)
            self.all.remove(card)
            self.trash_list.append(card)


    def discard(self, loc):
        card = self.hand.pop(loc)
        self.discard.append(card)

    def calc_points(self):
        sum2 = sum(card.points for card in self.all)
        # sum1 = 0
        # for card in self.all:
        #     sum1 +=card.points
        return sum2



def set_test():

    # start_deck = [c1,c2,c3,c4,c5,c6,c7,c8,c9]

    s = Set()
    print(s.__dict__.keys())
    print("Deck after shuffle: ")
    print(s.deck)
    
    s.end_turn()
    print("Hand:")
    print(s.hand)
    
    s.end_turn()
    print("Hand:")
    print(s.hand)
    
    print("----------------------")
    s.end_turn()
    print("Hand:")
    print(s.hand)
    
    s.end_turn()
    print("Hand:")
    print(s.hand)
    
    s.trash('hand',0)
    print(s.hand)
    
    print(s.calc_points())


# set_test()
