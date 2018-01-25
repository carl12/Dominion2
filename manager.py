from player import Player
from card import *
import string
class Manager:
    def __init__(self, store):
        self.store = store
        self.player = Player(self,self.store)
        self.name = "Superclass Manager"
        self.turns = 0



    def take_turn(self):
        self.turns +=1
        self.player.do_turn()

    def get_points(self):
        return self.player.get_points()

    def get_hand(self):
        return self.player.get_hand()

    def play(self, name):
        return self.player.play(name)

    def do_actions(self):
        return

    def get_all(self):
        return self.player.get_all()

    def get_left(self, name):
        return self.player.get_left(name)

    def card_prompt(self, card, requested_args):
        print('Base manager prompted')
        pass


class Human(Manager):

    def __init__(self, store, name="human"):
        super().__init__(store)
        self.name = name
        self.player = Player(self, store)

    def do_actions(self):
        actionPhase = True
        print('------------------------------')
        while self.player.actions > 0 and actionPhase:
            self.print_hand()
            a = input('Enter card to play ("end" to stop):').title()
            if a != 'End':
                if card_dict.get(a):
                    print('playing ', a)
                    self.play(a)

                else:
                    print('try again')
            else:
                actionPhase = False


    def buy_cards(self):
        buyPhase = True
        while self.player.buys > 0 and buyPhase:
            print(self.player.store_str())
            print("Buys: {}, Money: {} ".format(self.player.buys,self.player.money))
            a = input('Enter card to buy ("end" to stop):').title()
            if a != 'End':
                self.player.buy(a)
            else:
                buyPhase = False

    def card_prompt(self, card, requested_args):
        a = input('enter input for {}: '.format(card.name)).title()
        #store, card
        kwargs = {'card_choice':a}
        if card.use_effect(**kwargs):
            pass



    def print_hand(self):
        turn = self.player.turns
        act = self.player.actions
        buy = self.player.buys
        money = self.player.money
        print("Turn: {} || Actions: {}, Buys: {}, Money: {}"
            .format(turn,act,buy,money))
        print(self.get_hand())


class DumbMoney(Manager):
    num = 1
    def __init__(self,store, num=num):
        super().__init__(store)
        self.name = "DumbManager"+str(num)
        num +=1
        self.player = Player(self,self.store)


    def buy_cards(self):
        money = self.player.money
        if money >= 8:
            self.player.buy("Province")
        elif money >= 6:
            self.player.buy("Gold")
        elif money >= 3:
            card = self.player.buy("Silver")

class DumbMoneyV2(Manager):


    def __init__(self,store):
        super().__init__(store)
        self.name = "DumbManagerV2"
        self.player = Player(self,self.store)
        self.smithy= 0


    def buy_cards(self):
        money = self.player.money
        if self.smithy < 2 and money in (4,5):
            self.player.buy("Smithy")
            self.smithy+=1
        if money >= 8:
            self.player.buy("Province")
        elif money >= 6:
            self.player.buy("Gold")
        elif money >= 3:
            card = self.player.buy("Silver")

    def do_actions(self):
        hand = self.get_hand()
        have_smithy = any(isinstance(card,card_dict['Smithy']) for card in hand)
        if have_smithy:
            self.play("Smithy")


class DumbMoneyV3(Manager):
    def __init__(self,store):
        super().__init__(store)
        self.name = "DumbManagerV3"
        self.player = Player(self,self.store)
        self.smithy= 0

    def buy_cards(self):
        money = self.player.money
        if self.smithy < 2 and money in (4,5):
            self.player.buy("Smithy")
            self.smithy+=1
        if money >= 8:
            self.player.buy("Province")
        elif money >= 5 and self.get_left("Province") < 3:
            self.player.buy("Duchy")
        elif money >= 6:
            self.player.buy("Gold")
        elif money >= 3:
            card = self.player.buy("Silver")

    def do_actions(self):
        hand = self.get_hand()
        have_smithy = any(isinstance(card,card_dict['Smithy']) for card in hand)
        if have_smithy:
            self.play("Smithy")




