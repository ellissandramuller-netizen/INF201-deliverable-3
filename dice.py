import random

class Dice:
    """Representerer en trening med et valgfritt antall sider"""
    def __init__(self, sides=6):
        # Sjekker at terningen har misnt to sider
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides.")
        
        self.sides = sides

    def roll(self):
        """Kaster terningen og returnerer et tilfeldig tall"""
        return random.randint(1, self.sides)

    def __repr__(self):
        """Returnerer en tekstrepresentasjon av terningen"""
        return f"Dice(sides={self.sides})"

    def __call__(self):
        """Gjør at terningen kan kastes ved å kalle objektet direkte"""
        return self.roll()