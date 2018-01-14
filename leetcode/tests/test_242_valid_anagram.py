# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import unittest
from leetcode.s242_valid_anagram import Solution

class Test_242_Valid_Anagram(unittest.TestCase):

    def _is_anagram(self, s, t):
        solution = Solution()
        result = solution.isAnagram(s, t)
        return result

    def test_ab_ba_is_true(self):
        self.assertTrue(
            self._is_anagram("ab", "ba"))

    def test_ab_ac_is_false(self):
        self.assertFalse(
            self._is_anagram("ab", "ac"))

    def test_ab_ba_with_space_is_false(self):
        self.assertFalse(
            self._is_anagram("ab", "b a"))

if __name__ == "__main__":
    unittest.main()
