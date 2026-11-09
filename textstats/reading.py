"""Reading time estimate."""
import math


def reading_time(text: str, wpm: int = 200) -> int:
    """Minutes to read text at wpm words/minute (whitespace split), rounded up; 0 for blank text."""
    if wpm <= 0:
        raise ValueError("wpm must be positive")
    return math.ceil(len(text.split()) / wpm)
