import unittest

from textstats import word_count


class TestWordCount(unittest.TestCase):
    def check(self, text, n):
        self.assertEqual(word_count(text), n, repr(text))

    def test_separators(self):
        self.check("hello  world", 2)
        self.check("a\nb", 2)
        self.check("hello,world", 2)
        self.check("a\t\tb", 2)
        self.check("a b　c d", 4)
        self.check("a\r\n\r\nb", 2)

    def test_empty_and_only_separators(self):
        for t in ["", "   ", "\n\t ", "　", "...", ",;!?", " - ", "--", "-"]:
            self.check(t, 0)

    def test_leading_trailing_punctuation(self):
        self.check("  hello world  ", 2)
        self.check("...hello, world!!!", 2)
        self.check("(hi)", 1)

    def test_hyphen(self):
        self.check("well-known", 1)
        self.check("a well-known fact", 3)
        self.check("well-known,fact", 2)
        self.check("well-known\nfact", 2)
        self.check("-leading trailing-", 2)
        self.check("a--b", 2)
        self.check("a - b", 2)

    def test_unicode_words(self):
        self.check("héllo wörld", 2)
        self.check("你好 世界", 2)


if __name__ == "__main__":
    unittest.main()
