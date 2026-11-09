from character import Character

def play_round(hero: Character, enemy: Character):
    """Gjennomfører en kamprunde mellom helten og fienden"""
    hero.attack(enemy)

    # Fienden angriper tilbake hvis den fortsatt lever
    if enemy.is_alive:
        enemy.attack(hero)


def simulate_battle(hero: Character, enemy: Character):
    """Gjentar kamprundene helt til en av karakterene dør"""
    while hero.is_alive and enemy.is_alive:
        play_round(hero, enemy)