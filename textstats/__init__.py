"""Tiny text statistics used to exercise crew end to end."""
import re

# A word is alphanumeric runs joined by single internal hyphens.
_WORD = re.compile(r"[^\W_]+(?:-[^\W_]+)*")


def word_count(text: str) -> int:
    """Number of words in text."""
    return len(_WORD.findall(text))


def line_count(text: str) -> int:
    """Number of lines in text."""
    return len(text.split("\n"))


def char_count(text: str, include_spaces: bool = True) -> int:
    """Number of characters in text; whitespace (str.isspace) is skipped if include_spaces is False."""
    if include_spaces:
        return len(text)
    return sum(not c.isspace() for c in text)
