from random import randint

class Dice:
    ''' Class to module a Dice'''

    def __init__(self, sides = 6):
        self.sides = sides
    
    def roll_dice(self):
        randomNum = randint(1, self.sides)
        print(randomNum)


normal_dice = Dice(6)
tenSided_dice = Dice(10)
twentySided_dice = Dice(20)

for i in range(1, 10):
    normal_dice.roll_dice()

print("\n ------ \n ")

for i in range(1, 10):
    tenSided_dice.roll_dice()

print("\n ------ \n ")

for i in range(1, 10):
    twentySided_dice.roll_dice()

