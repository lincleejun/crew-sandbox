"""Tiny text statistics used to exercise crew end to end."""


def word_count(text: str) -> int:
    """Number of words in text."""
    return len(text.split(" "))


def line_count(text: str) -> int:
    """Number of lines in text."""
    return len(text.split("\n"))


def char_count(text: str, include_spaces: bool = True) -> int:
    """Number of characters in text; whitespace (str.isspace) is skipped if include_spaces is False."""
    if include_spaces:
        return len(text)
    return sum(not c.isspace() for c in text)
