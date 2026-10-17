"""Tiny text statistics used to exercise crew end to end."""


def word_count(text: str) -> int:
    """Number of words in text."""
    return len(text.split(" "))


def line_count(text: str) -> int:
    """Number of lines in text."""
    return len(text.split("\n"))
