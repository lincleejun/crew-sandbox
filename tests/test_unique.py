import unittest

from textstats.unique import unique_words


class TestUniqueWords(unittest.TestCase):
    def check(self, text, n):
        self.assertEqual(unique_words(text), n, repr(text))

    def test_case_insensitive(self):
        self.check("Hello hello HELLO", 1)
        self.check("The cat the CAT dog", 3)

    def test_punctuation(self):
        self.check("hello, hello! (hello)", 1)
        self.check("end. End? \"end\"", 1)
        self.check("don't dont", 2)  # inner punctuation kept
        self.check("hi -- hi", 1)  # pure-punctuation token is not a word

    def test_empty(self):
        for t in ["", "   ", "\n\t", "...", "-- !!"]:
            self.check(t, 0)


if __name__ == "__main__":
    unittest.main()
