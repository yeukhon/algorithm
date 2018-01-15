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


# The hash/dict approach performance:
#   n = length of nums1
#   m = length of nums2
#   adding to dictionary:   O(n) or O(m)
#   check recurrence:       O(n) or O(m)
#   total time complexity:  O(n+m)
#   storage complexity: O(g+k)
#       where g = size of intersect list
#       where k = size of common pool dictionary
#       In the worst case, when both input lists are equal, g and k is 2*length

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        intersect_list = []
        common_pool = {}

        for n in nums1:
            if n in common_pool:
                common_pool[n] += 1
            else:
                common_pool[n] = 1

        for n in nums2:
            if n in common_pool and common_pool[n] > 0:
                common_pool[n] -= 1
                intersect_list.append(n)
                if common_pool[n] == 0:
                    del common_pool[n]

        return intersect_list
