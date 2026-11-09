import string


def unique_words(text: str) -> int:
    """Distinct whitespace-separated words, edge punctuation stripped, case-insensitive."""
    words = {w.strip(string.punctuation).casefold() for w in text.split()}
    words.discard("")
    return len(words)
