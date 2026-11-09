import string


def longest_word(text: str) -> str:
    """Longest whitespace-separated word, edge punctuation stripped; first wins ties; "" if none."""
    return max((w.strip(string.punctuation) for w in text.split()), key=len, default="")
