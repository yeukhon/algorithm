# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/
# Given an array nums, write a function to move all 0's to the end of
# it while maintaining the relative order of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after calling your
# function, nums should be [1, 3, 12, 0, 0].
#
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
#
# Time complexity:
#   Our worst case is when we either have all zeros, or all non-zeros.
#   We can bound by O(n).

class Solution(object):
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        i = j = 0
        nums_len = len(nums)

        # set the first finger to the first zero (e.g. for input [1, 0]
        while i < nums_len and nums[i] != 0:
            i += 1

        # second finger is set right after first zero and then search
        # for a non-zero element
        j = i + 1

        # swap when we find the non-zero, and set first finger to the right
        while i < j and j < nums_len:
            if nums[j] != 0:
                self.swap(nums, i, j)
                i += 1
            j += 1

# better solution according to https://www.youtube.com/watch?v=xfxMOgurlAM
# complexity: O(n) regardless of how many zeroes or non-zeroes.
# the alternative solution proposed is 2 * non-zeroes
def moveZeroes(nums):
    if nums:
        start = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[start] = nums[i]
                start += 1
        while (start < len(nums)):
            nums[start] = 0
            start += 1

