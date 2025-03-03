"""This module is designed for the Wordle Game"""

__author__ = "730822741"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, char: str) -> bool:
    """Checks if the given single character is found in the given word."""
    assert len(char) == 1, f"len('{char}') is not 1"

    for letter in word:
        if letter == char:
            return True
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emojis representing the accuracy of the guess."""
    assert len(guess) == len(secret), "Guess and secret have to be in the same length"

    result = ""
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            result += (
                GREEN_BOX  # If the guessed character is exactly correct (same position)
            )
        elif contains_char(secret, guess[i]):
            result += (
                YELLOW_BOX  # If the character is in the word but in the wrong position
            )
        else:
            result += WHITE_BOX  # If the character is not in the word at all
    return result


def input_guess(expected_length: int) -> str:
    """Prompts the user for a guess of the correct length."""
    guess = input(f"Enter a {expected_length} character word: ")

    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")

    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns = 1
    max_turns = 6
    won = False

    while turns <= max_turns and not won:
        print(f"=== Turn {turns}/{max_turns} ===")
        guess = input_guess(
            len(secret)
        )  # Get a guess and ensure it has the right length
        result = emojified(guess, secret)
        print(result)

        if guess == secret:
            print(f"You won in {turns}/{max_turns} turns!")
            won = True
        else:
            turns += 1

    if not won:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
