"""Wordle-inspired game implementation."""

__author__ = "730822741"


def contains_char(word: str, char: str) -> bool:
    """Checks if the given character is in the word."""
    assert len(char) == 1, f"len('{char}') is not 1"
    return char in word


def emojified(guess: str, secret: str) -> str:
    """Returns emoji representation of guess compared to the secret word."""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
    return result


def input_guess(
    expected_length: int, predefined_input: list[str], input_index: int
) -> tuple[str, int]:
    """Receives a user guess from a predefined input list instead of input()."""
    while input_index < len(predefined_input):
        guess = predefined_input[input_index].strip()
        input_index += 1
        if len(guess) == expected_length:
            return guess, input_index
        print(f"That wasn't {expected_length} chars! Try again.")
    return "", input_index


def main(secret: str, predefined_input: list[str]) -> None:
    """Main game loop for Wordle implementation."""
    turns: int = 1
    max_turns: int = 6
    won: bool = False
    input_index: int = 0
    while turns <= max_turns and not won:
        print(f"=== Turn {turns}/{max_turns} ===")
        guess, input_index = input_guess(len(secret), predefined_input, input_index)
        if not guess:
            print("No more inputs available. Exiting game.")
            return
        print(emojified(guess, secret))
        if guess == secret:
            won = True
        else:
            turns += 1
    if won:
        print(f"You won in {turns} turns!")
    else:
        print("X/6 - Better luck next time!")


if __name__ == "__main__":
    predefined_inputs = ["codes", "guess", "world", "hello", "python", "codes"]
    main("codes", predefined_inputs)
