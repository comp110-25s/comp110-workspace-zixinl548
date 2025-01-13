"""My first exercise in COMP110!"""

__author__ = "730822741"


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello, " + name + "!"


if __name__ == "__main__":
    print(greet(name=input("What is your name? ")))

# Example outputs and explanation (commented out to avoid errors in execution):
# print(greet(name="Campers"))
# Output: "Hello, Campers!"
# None, but output to the screen: Hello, Campers!
