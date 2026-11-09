# Task 1
# Gitt kode fra oppgavebeskrivelseside i canvas:

# task 4 - added weapon as arg

# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon=None) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
            weapon: Optional weapon equipped by the character.
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        target.take_damage(self.damage)

    def take_damage(self, amount: int) -> None:
        """Reduce HP when the character takes damage"""
        self._hp = max(self._hp - amount, 0)

    def heal(self, amount: int) -> None:
        """Restore HP without exceeding maximum HP"""
        self._hp = min(self._hp + amount, self.hp_max)


    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Check whether the character is alive"""
        return self._hp > 0

# Task 3 

class Warrior(Character):
    """A character with armor that reduces incoming damage"""

    def __init__(self, name: str, hp_max: int = 100,
                 damage: int = 10, armor: int = 5) -> None:

        super().__init__(name, hp_max, damage)

        self.armor = armor

    def take_damage(self, amount: int) -> None:
        """Reduce incoming damage based on armor"""

        actual_damage = max(amount - self.armor, 0)
        super().take_damage(actual_damage)

class Mage(Character):
    """A character that uses mana for magical attacks"""

    def __init__(self, name: str, hp_max: int = 100,
                 damage: int = 10, mana: int = 30,
                 mana_max: int = 30) -> None:

        super().__init__(name, hp_max, damage)
        self.mana = mana
        self.mana_max = mana_max

    def attack(self, target) -> None:
        """Attack using magic when enough mana is available"""

        if self.mana >= 10:
            self.mana -= 10
            target.take_damage(self.damage * 2)
        else:
            super().attack(target)
            self.mana = min(self.mana + 5, self.mana_max)



