# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram
# Given two strings s and t, write a function to determine if t is
# an anagram of s.
#
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt
# your solution to such case?

# This classic, built-in sorting solution in Python is fine
# given the t and s are usually very small. Performance wise:
# sorted(string) -> O(n log n)
# ss == ts -> O(n) / O(1) if length is different
# total running complexity is probably: O(n + n.lg.n)

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        ss = sorted(s)
        ts = sorted(t)
        if ss == ts:
            return True
        else:
            return False
