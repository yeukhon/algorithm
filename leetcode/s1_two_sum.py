# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# (1). Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# Runtime: 3560 ms
class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        for i in range(nums_len-1):
            for j in range(i+1, nums_len):
                if nums[i] + nums[j] == target:
                    return [i, j]

# 24 ms
class Solution(object):
    def twoSum(self, nums, target):
        num_table = {}
        # one-pass hash table solution
        for i, num in enumerate(nums):
            if num in table:
                return [table[num], i]
            else:
                diff = target - num
                table[diff] = i
