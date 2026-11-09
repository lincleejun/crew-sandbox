import unittest

from textstats.frequency import word_frequency


class TestWordFrequency(unittest.TestCase):
    def test_order_by_count_then_alpha(self):
        text = "b a c b a b d"
        self.assertEqual(word_frequency(text, top=3), [("b", 3), ("a", 2), ("c", 1)])
        self.assertEqual(word_frequency("z y x", top=2), [("x", 1), ("y", 1)])
        self.assertEqual(word_frequency("a b a"), [("a", 2), ("b", 1)])  # default top=3, fewer words

    def test_case_and_punctuation(self):
        self.assertEqual(word_frequency("Hi, hi!", top=3), [("hi", 2)])
        self.assertEqual(word_frequency("(Cat) cat. CAT -- dog", top=3), [("cat", 3), ("dog", 1)])

    def test_empty_or_nonpositive_top(self):
        self.assertEqual(word_frequency("", top=3), [])
        self.assertEqual(word_frequency("   ...  ", top=3), [])
        self.assertEqual(word_frequency("a b", top=0), [])
        self.assertEqual(word_frequency("a b", top=-1), [])


if __name__ == "__main__":
    unittest.main()
