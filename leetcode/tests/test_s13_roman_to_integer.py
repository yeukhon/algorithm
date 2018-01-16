# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import unittest
from leetcode.s13_roman_to_integer import Solution

# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.

class Test_S13_Roman_To_Integer(unittest.TestCase):
    def create_solution(self, roman_numeral):
        solution = Solution()
        return solution.romanToInt(roman_numeral)

    def test_roman_numeral_1(self):
        output = self.create_solution("I")
        self.assertEqual(output, 1)

    def test_roman_numeral_4(self):
        output = self.create_solution("IV")
        self.assertEqual(output, 4)

    def test_roman_numeral_5(self):
        output = self.create_solution("V")
        self.assertEqual(output, 5)

    def test_roman_numeral_99(self):
        output = self.create_solution("XCIX")
        self.assertEqual(output, 99)

    def test_roman_numeral_100(self):
        output = self.create_solution("C")
        self.assertEqual(output, 100)

    def test_roman_numeral_207(self):
        output = self.create_solution("CCVII")
        self.assertEqual(output, 207)

    def test_roman_numeral_1000(self):
        output = self.create_solution("M")
        self.assertEqual(output, 1000)

    def test_roman_numeral_1066(self):
        output = self.create_solution("MLXVI")
        self.assertEqual(output, 1066)

    def test_roman_numeral_1200(self):
        output = self.create_solution("MCC")
        self.assertEqual(output, 1200)

    def test_roman_numeral_1234(self):
        output = self.create_solution("MCCXXXIV")
        self.assertEqual(output, 1234)

if __name__ == "__main__":
    unittest.main()
