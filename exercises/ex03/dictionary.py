"""Module for dictionary functions."""

__author__ = "730822741"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Invert keys and values in a dictionary. Raise KeyError for duplicate keys."""
    inverted_dict = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError("Duplicate value found when inverting dictionary.")
        inverted_dict[value] = key
    return inverted_dict


def count(input_list: list[str]) -> dict[str, int]:
    result_dict = {}
    for item in input_list:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] = 1
    return result_dict


def favorite_color(names_and_colors: dict[str, str]) -> str:
    if not names_and_colors:
        return None

    colors = list(names_and_colors.values())

    color_counts = count(colors)

    max_color = max(color_counts, key=color_counts.get)

    return max_color


def bin_len(strings: list[str]) -> dict[int, set[str]]:
    result = {}

    for s in strings:
        length = len(s)
        if length not in result:
            result[length] = set()
        result[length].add(s)
    return result
