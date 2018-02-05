# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import abc
import math

class BinaryHeapADT(object):
    """
    Abstract data type of a binary heap.

    :param keys: A list of priority keys for sorting priority.
    :type values: list
    :param values: A list of values associated with each
        key.
    :type values: list
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def insert(self, key, value):
        """
        Insert a new entry into the heap by providing a key
        and the entry's associated value.
        """
        return

    @abc.abstractmethod
    def pop(self):
        """
        Extract and remove the root of the heap.
        """
        return

    def parent_of(self, i):
        return int(math.floor(i/2))

    def children_of(self, i):
        return (2*i, 2*i +1)

    @abc.abstractmethod
    def ensure(self):
        """ Enssure the heap property is maintained. """
        return

    def __init__(self, keys, values):
        _keys = keys or [None]
        _values = values or [None]
        if _keys[0] is not None:
            _keys = [None] + _keys
        if _values[0] is not None:
            _values = [None] + _values
        self._keys = _keys
        self._values = _values
        self.ensure()

class MinBinaryHeap(BinaryHeapADT):
    """ Implements a min-(binary)-heap. """

    def min_heapify(self):
        x_index = 1
        smallest_index = 1
        smallest = self._keys[smallest_index]
        while smallest <= len(self._keys)-1:
            # get the children indices and find the smaller of the two
            l_index, r_index = self.children_of(smallest_index)
            if l_index <= len(self._keys)-1 and smallest > self._keys[l_index]:
                smallest, smallest_index = self._keys[l_index], l_index
            if r_index <= len(self._keys)-1 and smallest > self._keys[r_index]:
                smallest, smallest_index = self._keys[r_index], r_index
            if smallest == x_index:
                break
            else:
                self._keys[smallest_index], self._keys[x_index] = \
                    self._keys[x_index], self._keys[smallest_index]
                self._values[smallest_index], self._values[x_index] = \
                    self._values[x_index], self._values[smallest_index]
                x_index, smallest = smallest_index, self._keys[smallest]

    def ensure(self):
        """
        Visit the entire heap to ensure min-heap property is maintaed.
        """
        self.min_heapify()

    def pop(self):
        """
        Remove the root from the heap, which is the
        smallest item in the heap, based on the
        min-heap property.

        First, remove the key and the value from arrays. Next,
        fill the root with the last item in the arrays. Compare
        this element's key with its children, swap the smallest,
        repeat as many times as needed downward.
        """

        min_key, min_value = self._keys[1], self._values[1]
        self._keys[1], self._values[1] = self._keys[-1], self._values[-1]

        del self._keys[-1]
        del self._values[-1]

        self.min_heapify()
        return min_key, min_value

    def insert(self, key, value):
        """
        Insert a new entry into the heap.

        First, add the new entry (key and value) to the end of
        the arrays. Compare with the new entry's parent's key
        with the new entry's key and swap them if the new entry's
        key is smaller, repeat as many times as needed upward.

        :param key: The key for priority sorting comparsion.
        :param value: The value associatd with the key.

        """

        x_index = len(self._keys)
        xp_index = self.parent_of(x_index)
        self._keys.append(key)
        self._values.append(value)
        while xp_index >= 1 and \
              xp_index <= len(self._keys)-1 and \
              self._keys[x_index] < self._keys[xp_index]:
            self._keys[x_index], self._keys[xp_index] = \
                self._keys[xp_index], self._keys[x_index]
            self._values[x_index], self._values[xp_index] = \
                self._values[xp_index], self._values[x_index]
            x_index, xp_index = xp_index, self.parent_of(xp_index)


class MaxBinaryHeap(object):
    def __init__(self):
        self._data = [None]

    def get_size(self):
        """We always reserve the first."""
        return len(self._data) - 1

    def parent_of(self, i):
        return int(math.floor(i/2))

    def children_of(self, i):
        return 2*i, 2*i + 1

    def parent_is_smaller(self, x):
        parent_index = self.parent_of(x)
        return self._data[x] > self._data[parent_index]

    def swap(self, x_index, p_index):
        """Swap parent and child."""
        self._data[x_index], self._data[p_index] = (
            self._data[p_index], self._data[x_index])

    def insert(self, x):
        """Insert new data (x) into the end of the array,
        and let x bubbles upward until max heap order
        property is satisfied.

        """

        # remember we index 0 is always reserved, this is
        # important later on as we do insertion.
        self._data.append(x)
        x_index = self.get_size()
        xp_index = self.parent_of(x_index)

        while x_index > 1 and self.parent_is_smaller(x_index):
            self.swap(x_index, xp_index)
            x_index = xp_index
            xp_index = self.parent_of(x_index)

    def max_heapify(self, i):
        l_index, r_index = self.children_of(i)
        larger_index = i

        if (l_index <= self.get_size() and
            self._data[l_index] > self._data[i]):
            larger_index = l_index

        if (r_index <= self.get_size() and
            self._data[r_index] > self._data[larger_index]):
            larger_index = r_index

        if larger_index != i:
            self.swap(i, larger_index)
            self.max_heapify(larger_index)

    def pop(self):
        # heap is empty when the underlying list is left with
        # the first element in the list.
        if self.get_size() < 1:
            return None

        # swap max element which is at the root (index=1)
        # with the leaf node before popping.
        self.swap(1, self.get_size())

        # pop the max element and heapify from root
        # calling .pop() on a Python list will resize end of the list by 1
        val = self._data.pop()
        self.max_heapify(1)

        return val
