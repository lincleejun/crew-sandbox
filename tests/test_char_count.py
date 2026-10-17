import unittest

from textstats import char_count


class TestCharCount(unittest.TestCase):
    def test_default_and_explicit_true(self):
        self.assertEqual(char_count("a b\t\nc"), 6)
        self.assertEqual(char_count("a b\t\nc", True), 6)
        self.assertEqual(char_count("a b\t\nc", include_spaces=True), 6)

    def test_false_excludes_whitespace(self):
        self.assertEqual(char_count("a b\t\nc", False), 3)
        self.assertEqual(char_count("a b\t\nc", include_spaces=False), 3)

    def test_empty(self):
        self.assertEqual(char_count(""), 0)
        self.assertEqual(char_count("", False), 0)

    def test_only_whitespace(self):
        self.assertEqual(char_count("  \t\n", True), 4)
        self.assertEqual(char_count("  \t\n", False), 0)

    def test_unicode_whitespace(self):
        s = "a b　c d e"  # nbsp, ideographic, em space, line sep
        self.assertEqual(char_count(s), 9)
        self.assertEqual(char_count(s, False), 5)

    def test_unicode_chars(self):
        self.assertEqual(char_count("你好 é", False), 3)


if __name__ == "__main__":
    unittest.main()
