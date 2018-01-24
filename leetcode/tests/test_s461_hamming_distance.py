# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import unittest
import collections

from leetcode.s461_hamming_distance import Solution

# 461. Hamming Distance
# https://leetcode.com/problems/hamming-distance/

Fixture = collections.namedtuple(
    'Fixture', ['x', 'y', 'ans'])

fixtures = [
    Fixture(x=1, y=4, ans=2),
    Fixture(x=1, y=128, ans=2),
    Fixture(x=40, y=321, ans=5)
]


class Test_S461_Hamming_Distance(unittest.TestCase):

    def get_result(self, fixture):
        s = Solution()
        return s.hammingDistance(
            fixture.x, fixture.y)

    def test_1_4(self):
        fixture_1 = fixtures[0]
        self.assertEqual(
            self.get_result(fixture_1),
            fixture_1.ans)

    def test_1_128(self):
        fixture_2 = fixtures[1]
        self.assertEqual(
            self.get_result(fixture_2),
            fixture_2.ans)

    def test_40_321(self):
        fixture_3 = fixtures[2]
        self.assertEqual(
            self.get_result(fixture_3),
            fixture_3.ans)

if __name__ == "__main__":
    unittest.main()
