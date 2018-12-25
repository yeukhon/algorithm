# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

import unittest

from leetcode.s1_two_sum import Solution

class TestTwoSum(unittest.TestCase):
    def test_default_case(self):
        array = [2, 7, 11, 15]
        target = 9
        answer = Solution().twoSum(array, target)
        self.assertEqual(answer, [0, 1])

    def test_empty_array(self):
        array = []
        target = 9
        answer = Solution().twoSum(array, target)
        self.assertEqual(answer, None)

    def test_single_element_array(self):
        array = [1]
        target = 1
        answer = Solution().twoSum(array, target)
        self.assertEqual(answer, None)

    def test_two_element_array_no_match(self):
        array = [1, 2]
        target = 1
        answer = Solution().twoSum(array, target)
        self.assertEqual(answer, None)

    def test_two_element_array_has_match(self):
        array = [1, 2]
        target = 3
        answer = Solution().twoSum(array, target)
        self.assertEqual(answer, [0, 1])

    def test_3_2_4(self):
        array = [3, 2, 4]
        target = 6
        answer = Solution().twoSum(array, target)
        self.assertEqual(answer, [1, 2])

if __name__ == '__main__':
    unittest.main()
