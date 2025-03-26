"""Tests for dictionary functions."""

__author__ = "730822741"

import pytest

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


# Tests for invert
def test_invert_edge_case():
    """Edge case: Test inverting an empty dictionary."""
    assert invert({}) == {}


def test_invert_use_case1():
    """Use case: Invert a dictionary with unique values."""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_use_case2():
    """Use case: Test inverting a dictionary with multi-character keys and values."""
    assert invert({"apple": "banana", "car": "train"}) == {
        "banana": "apple",
        "train": "car",
    }


# Tests for count
def test_invert_raises_key_error():
    """Test that invert raises a KeyError when duplicate values exist."""
    with pytest.raises(KeyError):
        invert({"kris": "jordan", "michael": "jordan"})


def test_count_edge_case():
    """Edge case: Test an empty list."""
    assert count([]) == {}


def test_count_use_case1():
    """Use case: Test a list with repeated and unique values."""
    assert count(["apple", "banana", "apple", "orange", "banana", "apple"]) == {
        "apple": 3,
        "banana": 2,
        "orange": 1,
    }


def test_count_use_case2():
    """Use case: Test a list with no repeated values."""
    assert count(["a", "b", "c"]) == {"a": 1, "b": 1, "c": 1}


def test_count_single_item():
    """Use case: Test a list with one item repeated multiple times."""
    assert count(["apple", "apple", "apple"]) == {"apple": 3}


# Tests for favorite_color
def test_favorite_color_edge_case():
    """Edge case: Test an empty dictionary."""
    assert favorite_color({}) == None  # None or any other value for no input


def test_favorite_color_no_tie():
    """Use case: Test a list where one color is most frequent."""
    assert favorite_color({"Alice": "blue", "Bob": "red", "Charlie": "blue"}) == "blue"


def test_favorite_color_with_tie():
    """Use case: Test a list with a tie for most frequent color."""
    assert favorite_color({"Alice": "blue", "Bob": "blue", "Charlie": "red"}) == "blue"


def test_favorite_color_all_same():
    """Use case: Test when all colors are the same."""
    assert favorite_color({"Alice": "blue", "Bob": "blue", "Charlie": "blue"}) == "blue"


# Tests for bin_len
def test_bin_len_basic_case():
    """Test basic case with mixed lengths."""
    result = bin_len(["the", "quick", "fox"])
    expected = {3: {"the", "fox"}, 5: {"quick"}}
    assert result == expected


def test_bin_len_duplicate_strings():
    """Test case with duplicate strings."""
    result = bin_len(["the", "the", "fox"])
    expected = {3: {"the", "fox"}}
    assert result == expected


def test_bin_len_empty_list():
    """Edge case: Test with an empty list."""
    result = bin_len([])
    expected = {}
    assert result == expected
