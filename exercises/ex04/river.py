from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    def __init__(self, num_fish: int, num_bears: int):
        self.day = 0
        self.fish = [Fish() for _ in range(num_fish)]
        self.bears = [Bear() for _ in range(num_bears)]

    # Modify check_ages method to remove old animals
    def check_ages(self):
        """Remove old animals from the river"""
        # Remove old Fish (age > 3)
        self.fish = [fish for fish in self.fish if fish.age <= 3]

        # Remove old Bears (age > 5)
        self.bears = [bear for bear in self.bears if bear.age <= 5]

    # Method to remove fish from the river
    def remove_fish(self, amount: int):
        """Remove 'amount' many Fish from the front"""
        self.fish = self.fish[amount:]  # Slice the list to remove frontmost fish

    def one_river_week(self):
        for _ in range(7):
            self.one_river_day()

    def bears_eating(self):
        """Simulate bears eating fish"""
        for bear in self.bears:
            if len(self.fish) >= 5:  # Ensure there are at least 5 fish in the river
                bear.eat(3)  # Bear eats 3 fish
                self.remove_fish(3)  # Remove 3 fish from the river

    def check_hunger(self):
        """Remove hungry bears (hunger_score < 0) from the river"""
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]

    def repopulate_fish(self):
        """Repopulate fish: each pair of fish will produce 4 offspring"""
        new_fish = (len(self.fish) // 2) * 4  # Each pair of fish produces 4 offspring
        self.fish.extend([Fish() for _ in range(new_fish)])  # Add new fish to the river

    def repopulate_bears(self):
        """Repopulate bears: each pair of bears will produce 1 offspring"""
        new_bears = len(self.bears) // 2  # Each pair of bears produces one offspring
        self.bears.extend(
            [Bear() for _ in range(new_bears)]
        )  # Add new bears to the river

    def view_river(self) -> None:  # Updated to print the river status
        """Print the current day and population numbers."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
