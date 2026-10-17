import unittest

from textstats import line_count, word_count


class TestTextstats(unittest.TestCase):
    def test_word_count_simple(self):
        self.assertEqual(word_count("hello world"), 2)

    def test_line_count(self):
        self.assertEqual(line_count("a\nb"), 2)


if __name__ == "__main__":
    unittest.main()
