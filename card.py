

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
    is_action = True
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

class PromptActionCard(ActionCard):
    use_args = None
    def play(self):
        super(PromptActionCard, self).play()
        self.prompt_player()

    def prompt_player(self):
        self.owner.card_prompt(self, self.use_args)

    def use_effect(self):
        print('promptactioncard card_effect called :( ')
        pass

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
    money = 2
    buy = 1

class Feast(PromptActionCard):
    cost = 4
    use_args = ['store','card_choice']

    def use_effect(self, **kwargs):
        print('Feast processing card_effect response')
        store = 'store'
        card_choice = 'card_choice'

        added_card = None
        if store in kwargs and card_choice in kwargs:
            card_str = kwargs[card_choice]
            game_store = kwargs[store]

            card_ref = card_dict[card_str]
            if card_ref and card_ref.cost <= 5:
                added_card = game_store.take(card_str)
            print(added_card)
            if added_card:
                self.owner.set.gain(added_card(self.owner))
                self.owner.set.trash('in_play', 0)
                return True
        raise Exception('Feast did not work')





class Gardens(VictoryCard):
    cost = 4
    @property
    def points(self):
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