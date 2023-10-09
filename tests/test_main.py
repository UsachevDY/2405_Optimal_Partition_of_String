from unittest import TestCase

from main import Solution


class TestSolution(TestCase):

    def test_1(self):
        data = "abacaba"
        expected = 4
        result = Solution().partitionString(data)
        self.assertEqual(expected, result)

    def test_2(self):
        data = "ssssss"
        expected = 6
        result = Solution().partitionString(data)
        self.assertEqual(expected, result)

    def test_3(self):
        data = "a"
        expected = 1
        result = Solution().partitionString(data)
        self.assertEqual(expected, result)

    def test_4(self):
        data = "ThisIsmyString".lower()
        expected = 3
        result = Solution().partitionString(data)
        self.assertEqual(expected, result)

    def test_5(self):
        data = "a" * (10 ^ 5)
        expected = len(data)
        result = Solution().partitionString(data)
        self.assertEqual(expected, result)

    def test_6(self):
        data = "TwoposSiblePartItIonsare".lower()
        expected = 5
        result = Solution().partitionString(data)
        self.assertEqual(expected, result)