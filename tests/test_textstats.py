import unittest

from textstats import line_count, word_count


class TestTextstats(unittest.TestCase):
    def test_word_count_simple(self):
        self.assertEqual(word_count("hello world"), 2)

    def test_line_count(self):
        self.assertEqual(line_count("a\nb"), 2)

    def test_line_count_empty(self):
        self.assertEqual(line_count(""), 0)

    def test_line_count_trailing_newline(self):
        self.assertEqual(line_count("a\nb\n"), 2)


if __name__ == "__main__":
    unittest.main()
