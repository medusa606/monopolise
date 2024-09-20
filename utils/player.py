from utils import constants
from utils import dice


class Player:
    name = 'unnamed'
    properties = []
    no_sites = 0
    no_houses = 0
    balance: int = 0
    position: int = 1
    d1: int
    d2: int
    double: bool = False
    BANKRUPT: bool = False
    meeple = ''
    id = 0
    doubles_rolled: int = 0
    in_jail: bool = False
    remaining_sentence = 0
    chance_id = -1
    site_colours = dict(brown=0, blue=0, pink=0, orange=0, red=0, yellow=0, green=0, purple=0, station=0, utility=0)
    complete_set = dict(brown=False, blue=False, pink=False, orange=False, red=False, yellow=False, green=False, purple=False, station=False, utility=False)
    asset_value = 0

    def __init__(self, name, meeple=None):
        self.name = name
        self.balance = constants.starting_balance
        self.meeple = meeple

    def roll_dice(self, Dice):
        d1, d2 = Dice.roll_dice()
        self.d1 = d1
        self.d2 = d2
        if d1 == d2:
            self.double = True
            self.roll_double()
            return True
        else:
            self.double = False
            return False

    def move(self):
        self.position += (self.d1 + self.d2)
        if self.position >40:
            self.position -= 40
            # print(f"{self.name} passes GO and receives £{constants.passes_go_credit}")
            self.transaction(constants.passes_go_credit)

    def to_jail(self):
        self.in_jail = True
        self.position = 10
        self.remaining_sentence = 3

    def out_jail(self):
        self.in_jail = False
        self.remaining_sentence = 0

    def transaction(self, value):
        self.balance += value

    def roll_double(self):
        self.doubles_rolled += 1
        if self.doubles_rolled > 2:
            # print(f"{self.name} has rolled 3 doubles and must go to Jail")
            self.doubles_rolled = 0
            self.to_jail()
