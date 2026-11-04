from dice import Dice

class Weapon:
    def __init__(self, name, damage_dice: Dice):
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self):
        return self.damage_dice.roll()