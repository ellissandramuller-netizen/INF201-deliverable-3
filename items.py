from dice import Dice

class Weapon:
    """Representerer et våpen som bruker en terning til å beregne skade"""
    def __init__(self, name, damage_dice: Dice):
        # Lagrer navnet på våpenet og hvilken terning den bruker
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self):
        # Kaster terningen for å bestemme skaden som våpenet gjør
        return self.damage_dice.roll()