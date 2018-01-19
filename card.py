

class Card:
    cost = 0
    draw = 0
    action = 0
    buy = 0
    money = 0
    point_chips = 0
    points = 0
    is_action = False
    is_vp = False
    is_treasure= False

    def __init__(self, owner, game=None, opponents=None):
        self.game = game
        self.owner=owner
        self.opponents=opponents

    def __repr__(self):
        return type(self).__name__

    @property
    def name(self):
        return type(self).__name__

    def play(self):
        return
        #add all respective stuff to owner


class ActionCard(Card):
    def __init__(self, owner, game=None, opponents=None):
        self.game = game
        self.owner=owner
        self.opponents=opponents

    def play(self):
        self.owner.actions += self.action - 1
        self.owner.buys += self.buy
        self.owner.money += self.money
        self.owner.point_chips += self.point_chips
        self.owner.draw(self.draw)
        
        # self.owner.points += points



    is_action = True

class VictoryCard(Card):
    is_vp = True

class TreasureCard(Card):
    is_treasure = True

    def play(self):
        self.owner.money += self.money



class Village(ActionCard):
    cost = 3
    draw = 1
    action = 2
    name = "Village"

class Smithy(ActionCard):
    cost = 4
    draw = 3
    name = "Smithy"

class Festival(ActionCard):
    cost = 5
    action = 2
    buy = 1
    money = 2
    name = "Festival"

class Laboratory(ActionCard):
    cost = 5
    draw = 2
    action = 1

class Market(ActionCard):
    cost = 5
    draw = 1
    action = 1
    buy = 1
    money = 1

class Woodcutter(ActionCard):
    cost = 3
    actino = 1
    money = 2

class Gardens(VictoryCard):
    cost = 4
    @property
    def cost(self):
        print('calculate garden value')

class Copper(TreasureCard):
    money = 1

class Silver(TreasureCard):
    money = 2
    cost = 3

class Gold(TreasureCard):
    money = 3
    cost = 6

class Estate(VictoryCard):
    points = 1
    cost = 2

class Duchy(VictoryCard):
    points = 3
    cost = 5

class Province(VictoryCard):
    points = 6
    cost = 8



def attribute_test():
    card = Card()
    smithy = Smithy()
    village = Village()

    print(smithy.action)
    print(smithy.draw)
    print(smithy.money)


# from set import Set
super_classes = ('Card','ActionCard','VictoryCard')
g = locals().copy()
card_dict = {}
for key, vals in g.items():
    if type(vals) is type and key not in super_classes:
        card_dict[key] = vals
# print(available_cards)
# print(card_dict)