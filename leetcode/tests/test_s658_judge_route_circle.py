# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import unittest
import collections

from leetcode.s657_judge_route_circle import Solution

# 657. Judge Route Circle
# https://leetcode.com/problems/judge-route-circle/

class Test_s657_Judge_Route_Circle(unittest.TestCase):
    def get_result(self, moves):
        s = Solution()
        return s.judgeCircle(moves)

    def test_up_down_is_circle(self):
        self.assertTrue(
            self.get_result('UD'),
        )

    def test_up_up_is_not_circle(self):
        self.assertFalse(
            self.get_result('UU')
        )

    def test_down_down_is_not_circle(self):
        self.assertFalse(
            self.get_result('DD')
        )

    def test_down_up_up_down_is_circle(self):
        self.assertTrue(
            self.get_result('DUUD')
        )

    def test_left_right_is_circle(self):
        self.assertTrue(
            self.get_result('LR')
        )

    def test_right_left_is_circle(self):
        self.assertTrue(
            self.get_result('RL')
        )

    def test_left_left_is_not_circle(self):
        self.assertFalse(
            self.get_result('LL')
        )

    def test_left_right_down_up_is_circle(self):
        self.assertTrue(
            self.get_result('LRDU')
        )

    def test_left_right_right_left_up_right_is_not_circle(self):
        self.assertFalse(
            self.get_result('LRRLUR')
        )

if __name__ == "__main__":
    unittest.main()
