# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# 350. Intersection of Two Arrays II
# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
#
# Note:
#  - Each element in the result should appear as many times as it shows
#    in both arrays.
#  - The result can be in any order.
#
# Follow up:
#
#  - What if the given array is already sorted? How would you optimize
#    your algorithm?
#  - What if nums1's size is small compared to nums2's size? Which
#    algorithm is better?
#  - What if elements of nums2 are stored on disk, and the memory
#    is limited such that you cannot load all elements into the memory at once?


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nums1_length = len(nums1)
        nums2_length = len(nums2)

        if nums1_length >= nums2_length:
            longer_list = nums1
            shorter_list = nums2
        else:
            longer_list = nums2
            shorter_list = nums1

        return [s for s in shorter_list if s in longer_list]
