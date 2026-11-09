import unittest

from textstats.sentences import sentence_count


class TestSentenceCount(unittest.TestCase):
    def check(self, text, n):
        self.assertEqual(sentence_count(text), n, repr(text))

    def test_empty(self):
        for t in ["", "   ", "\n"]:
            self.check(t, 0)

    def test_single(self):
        self.check("Hello world.", 1)
        self.check("Hello world", 1)
        self.check("你好。", 1)

    def test_multiple(self):
        self.check("One. Two! Three?", 3)
        self.check("一。二！三？", 3)

    def test_consecutive_punctuation(self):
        self.check("Wait... What?!", 2)
        self.check("真的吗？！是的。。。", 2)
        self.check("...", 0)

    def test_mixed(self):
        self.check("Hello. 你好！How are you? 我很好。", 4)
        self.check("中文句子。English sentence! 混合？？", 3)


if __name__ == "__main__":
    unittest.main()
