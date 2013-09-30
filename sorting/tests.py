# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import random
import unittest

import insertion

def random_list():
    return random.sample(range(100), 100)  

class TestInsertionSort(unittest.TestCase):
    def _test_true_false(self, ulist, expectation):
        slist = insertion.insertion_sort(ulist)
        self.assertEqual(slist, expectation)
    
    def _test_eq(self, ulist):
        slist = insertion.insertion_sort(ulist)
        expected = sorted(ulist)
        self.assertEqual(slist, expected)

    def test_21453_to_sorted(self):
        self._test_true_false([2,1,4,5,3], [1,2,3,4,5])
        
    def test_12345_to_sorted(self):
        self._test_true_false([1,2,3,4,5], [1,2,3,4,5])

    def test_121_to_sorted(self):
        self._test_true_false([1,2,1], [1,1,2])

    def test_random_list(self):
        self._test_eq(random_list())
    
