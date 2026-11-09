import unittest

from textstats.reading import reading_time


class TestReadingTime(unittest.TestCase):
    def test_rounds_up(self):
        self.assertEqual(reading_time("w " * 200), 1)
        self.assertEqual(reading_time("w " * 201), 2)
        self.assertEqual(reading_time("w " * 10, wpm=3), 4)

    def test_nonempty_at_least_one_minute(self):
        self.assertEqual(reading_time("hello"), 1)

    def test_blank_is_zero(self):
        for t in ["", "   ", "\n\t "]:
            self.assertEqual(reading_time(t), 0, repr(t))

    def test_bad_wpm(self):
        for wpm in [0, -1]:
            with self.assertRaises(ValueError):
                reading_time("hello", wpm=wpm)


if __name__ == "__main__":
    unittest.main()
