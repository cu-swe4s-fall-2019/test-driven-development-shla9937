import unittest
import random
import os
import math_lib
import statistics


class TestMathLib(unittest.TestCase):

    def test_find_easy_mean(self):
        L = [1, 2, 3]
        r = math_lib.list_mean(L)
        self.assertEqual(r, 2)

    def test_find_float_mean(self):
        L = [1.3, 2.6, 3.6]
        r = math_lib.list_mean(L)
        self.assertEqual(r, 2.5)

    def test_find_random_mean(self):
        L = []
        for j in range(100):
            for i in range(100):
                rand_int = random.randint(1, 100)
                L.append(rand_int)
            r = math_lib.list_mean(L)
            answer = statistics.mean(L)
            self.assertEqual(r, answer)

    def test_find_easy_stdev(self):
        L = [2, 2, 2]
        r = math_lib.list_stdev(L)
        self.assertEqual(r, 0)

    def test_find_float_stdev(self):
        L = [1.3, 2.6, 3.6]
        r = math_lib.list_stdev(L)
        answer = statistics.stdev(L)
        self.assertAlmostEqual(r, answer)

    def test_find_random_stdev(self):
        L = []
        for j in range(100):
            for i in range(100):
                rand_int = random.randint(1, 100)
                L.append(rand_int)
            r = math_lib.list_stdev(L)
            answer = statistics.stdev(L)
            self.assertAlmostEqual(r, answer)


if __name__ == '__main__':
    unittest.main()
