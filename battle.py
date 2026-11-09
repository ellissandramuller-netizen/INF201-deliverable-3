from character import Character

class Battle:
    """Representerer en kamp mellom to karakterer"""

    def __init__(self, hero: Character, enemy: Character):
        """Oppretter en kamp mellom helten og fienden"""
        self.hero = hero
        self.enemy = enemy

    def play_round(self):
        """Gjennomfører en kamprunde mellom helten og fienden"""
        self.hero.attack(self.enemy)

        # Fienden angriper tilbake hvis den fortsatt lever
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)


    def simulate_battle(self):
        """Gjentar kamprundene helt til en av karakterene dør"""
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()