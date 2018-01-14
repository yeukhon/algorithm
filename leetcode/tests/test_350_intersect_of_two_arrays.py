# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import unittest
from leetcode.s350_intersect_of_two_arrays import Solution

class Test_350_Intersect_of_Two_Arrays(unittest.TestCase):

    def _intersect(self, a1, a2):
        solution = Solution()
        result = solution.intersect(a1, a2)
        return result

    def test_12_13_returns_1(self):
        self.assertEqual(
            self._intersect([1,2], [1,3]), [1])

    def test_10_45_returns_empty_list(self):
        self.assertEqual(
            self._intersect([1,0], [4,5]), [])

    def test_12221_22_returns_22(self):
        self.assertEqual(
            self._intersect([1,2,2,1], [2,2]), [2, 2])

    def test_12_11_returns_1(self):
        self.assertEqual(
            self._intersect([1,2], [1,1]), [1])

if __name__ == "__main__":
    unittest.main()
