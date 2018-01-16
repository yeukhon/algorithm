# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):

    numeral_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int

        A new symbol is used every time we reached 5 and 10. For example,
        for range(1-10), we can uniquely identify:
            1..4 -> I
            5..9 -> V+
            10   -> X

        So if we have "IV", we know it must fall within the integer 1..4,
        since I is the leading character; when V is the leading character,
        we know integer k is (5 >= k < 10)

        With this knowledge, we don't have to list all of the roman numeral
        symbols (1-9, 10-90, 100-1000).


        Now, to convert from roman numeral to integer, we scan through each
        numeral character, and lookup the value in the mapping table. The
        trick is to remember the last character scanned. Given "IV",
        the first pass sees "I" and we remember the value of "I". Then,
        in the next pass the algorithm sees "V". Since the value of "I"
        is less than the value of "V", we know, again, as described
        above, "IV" must be in the lower range. With this knowledge,
        we do a subtraction:
            V - I ==>  5 - 1 ==> 4  (which is IV)

        However, if we are given XI as an input. The first scan sees
        "X" (10), and in the next pass we see I (1), then we learn
        we have just finished the upper range, and we can safely add
        up I.

            X + I ==>  10 + 1 ==> 11 (which is XI)
        """

        lookback_value = total = 0

        for c in s:
            c_value = self.numeral_map[c]
            if c in self.numeral_map:
                if lookback_value < c_value and total != 0:
                    total = (total - lookback_value)
                    total += c_value - lookback_value
                    lookback_value = c_value
                else:
                    total += c_value
                    lookback_value = c_value
        return total
