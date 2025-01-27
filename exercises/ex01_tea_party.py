"""This program calculates the quantity of tea bags needed, treats, and the expected cost for a tea party."""

# blank line for clarity
__author__: str = "730822741"


def main_planner(guests: int) -> None:
    """Plan and print the details for the tea party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Calculate the number of tea bags needed based on the number of guests. Each person is expected to drink two cups of tea, requiring two tea bags."""
    return people * 2


def treats(people: int) -> int:
    """Calculate the number of treats needed based on the number of teas guests will drink. Assumes each tea requires 1.5 treats."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the total cost of tea bags and treats combined. Assumes each tea bag costs $0.50 and each treat costs $0.75."""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
