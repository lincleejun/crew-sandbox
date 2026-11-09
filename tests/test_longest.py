import unittest

from textstats.longest import longest_word


class TestLongestWord(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(longest_word("a bb ccc"), "ccc")

    def test_tie_takes_first(self):
        self.assertEqual(longest_word("cat dog\tant"), "cat")

    def test_strips_edge_punctuation(self):
        self.assertEqual(longest_word("hi, (world!!!) ok"), "world")
        self.assertEqual(longest_word("abcd... xyz"), "abcd")

    def test_empty(self):
        self.assertEqual(longest_word(""), "")
        self.assertEqual(longest_word("   \n"), "")
        self.assertEqual(longest_word("... !!"), "")


if __name__ == "__main__":
    unittest.main()
