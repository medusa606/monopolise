import random
from utils import constants

# for debugging
from icecream import ic
# random.seed = 0

class Chance():
    cards = []
    outcome = ''

    def __init__(self):
        self.cards = ['Advance to Go (Collect £200)',
                      'Advance to Trafalgar Square. If you pass Go, collect £200',
                      'Advance to Mayfair',
                      'Advance to Pall Mall. If you pass Go, collect £200',
                      'Advance to the nearest Station. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled',
                      'Advance to the nearest Station. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled',
                      'Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.',
                      'Bank pays you dividend of £50',
                      'Get Out of Jail Free',
                      'Go Back 3 Spaces',
                      'Go to Jail. Go directly to Jail, do not pass Go, do not collect £200',
                      'Make general repairs on all your property. For each house pay £25. For each hotel pay £100',
                      'Speeding fine £15',
                      'Take a trip to Kings Cross Station. If you pass Go, collect £200',
                      'You have been elected Chairman of the Board. Pay each player £50',
                      'Your building loan matures. Collect £150', ]

    def deal_card(self, Player):
        id = random.randint(0, 1)  #15
        # print(f"{Player.name} receives card: {self.cards[id]}")
        Player.chance_id = id

        if id == 0:
            Player.position = 1
            self.outcome = f"{Player.name} passes GO and receives £{constants.passes_go_credit}"
            Player.transaction(constants.passes_go_credit)
        elif id == 1:
            if Player.position < 25:
                Player.position = 25
                self.outcome = f"{Player.name} moves to Trafalgar Square"
            if Player.position > 25:
                Player.position = 25
                self.outcome = f"{Player.name} moves to Trafalgar Square, passes GO and gets £{constants.passes_go_credit}"
                Player.transaction(constants.passes_go_credit)
        elif id == 2:
            Player.position = 40
            self.outcome = f"{Player.name} moves to Mayfair"