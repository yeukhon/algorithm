# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import unittest
from leetcode.s283_move_zeroes import Solution

class Test_283_Move_Zeroes(unittest.TestCase):

    def get_result(self, array):
        s = Solution()
        s.moveZeroes(array)

    def test_empty_array(self):
        a = []
        self.get_result(a)
        self.assertEqual(0, len(a))

    def test_1_array(self):
        a = [1]
        self.get_result(a)
        self.assertEqual(a, [1])

    def test_0_array(self):
        a = [0]
        self.get_result(a)
        self.assertEqual(a, [0])

    def test_0_1_array(self):
        a = [0, 1]
        self.get_result(a)
        self.assertEqual(a, [1, 0])

    def test_1_0_array(self):
        a = [1, 0]
        self.get_result(a)
        self.assertEqual(a, [1, 0])

    def test_1_0_0_array(self):
        a = [1, 0, 0]
        self.get_result(a)
        self.assertEqual(a, [1, 0, 0])

    def test_1_2_0_array(self):
        a = [1, 2, 0]
        self.get_result(a)
        self.assertEqual(a, [1, 2, 0])

    def test_0_0_1_array(self):
        a = [0, 0, 1]
        self.get_result(a)
        self.assertEqual(a, [1, 0, 0])

    def test_0_1_0_array(self):
        a = [0, 1, 0]
        self.get_result(a)
        self.assertEqual(a, [1, 0, 0])

    def test_1_0_2_array(self):
        a = [1, 0, 2]
        self.get_result(a)
        self.assertEqual(a, [1, 2, 0])

    def test_1_3_0_0_5_9_0_4_1(self):
        a = [1, 3, 0, 0, 5, 9, 0, 4, 1]
        self.get_result(a)
        self.assertEqual(a, [1, 3, 5, 9, 4, 1, 0, 0, 0])

if __name__ == "__main__":
    unittest.main()
