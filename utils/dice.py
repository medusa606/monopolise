''' A class to generate dice rolls and keep history
'''
import random

# for dice histogram
import matplotlib.pyplot as plt
import numpy as np
# random.seed = 0

class Dice:
    dice_1 = 0
    dice_2 = 0
    dice_history = []

    # method to roll dice
    def roll_dice(self):
        dice1 = random.randrange(1, 7)
        dice2 = random.randrange(1, 7)
        self.dice_history.append(dice1)
        self.dice_history.append(dice2)
        self.dice_1 = dice1
        self.dice_2 = dice2
        return dice1, dice2

# # create a dice object
# die = Dice()
# for i in range(100):
#     d1, d2 = die.roll_dice()
#
# # roll n time and plot histogram
# plt.hist(np.array(die.dice_history), bins=6, color='skyblue', edgecolor='black')
# plt.title(f"Die histogram for {len(die.dice_history)} rolls")
# plt.show()