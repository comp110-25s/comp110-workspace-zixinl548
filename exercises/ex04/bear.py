"""File to define Bear class."""


class Bear:
    def __init__(self):
        self.age = 0
        self.hunger_score = 0  # Initialize hunger_score to 0

    def one_day(self):
        """Simulate one day in the bear's life"""
        self.age += 1
        self.hunger_score -= 1  # Decrease hunger score by 1 each day

    def eat(self, num_fish: int):
        """Increase hunger_score by the number of fish eaten"""
        self.hunger_score += num_fish
