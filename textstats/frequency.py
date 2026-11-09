import string
from collections import Counter


def word_frequency(text: str, top: int = 3) -> list[tuple[str, int]]:
    """Top `top` (word, count) pairs: whitespace-split, edge punctuation stripped, case-insensitive; count desc, then word asc."""
    if top <= 0:
        return []
    counts = Counter(w.strip(string.punctuation).casefold() for w in text.split())
    counts.pop("", None)
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:top]
