import unittest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lottery_function import lottery

class TestLotteryFunction(unittest.TestCase):
    def test_lottery_function(self):
        self.assertEqual(lottery([1, 1, 3, 2, 2, 2, 4, 5], 2), [1])
        self.assertEqual(lottery([1, 1, 2, 2, 2, 3, 4, 5], 3), [2])
        self.assertEqual(lottery([1, 2, 2, 2, 3, 4, 5, 5, 1], 2), [1, 5])
        self.assertEqual(lottery(None, 1), [])
        self.assertEqual(lottery([1, 2, 3], None), [])
        self.assertEqual(lottery(None, None), [])
        self.assertEqual(lottery([1, 1, 2, 2, 2, 3, 4, 5], 7), [])
if __name__ == '__main__':
    unittest.main()