"""Sentence counting."""
import re

# A run of terminators (. ! ? 。 ！ ？) ends one sentence.
_END = re.compile(r"[.!?。！？]+")


def sentence_count(text: str) -> int:
    """Number of sentences: non-blank segments between terminator runs (trailing text without one counts)."""
    return sum(bool(s.strip()) for s in _END.split(text))
