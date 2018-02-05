import random
import unittest

from algorithm.heap.heap import MinBinaryHeap, MaxBinaryHeap

class TestMinBinaryHeap(unittest.TestCase):
    def setUp(self):
        self.keys = [2,3,4]
        self.values = ["b", "d", "c"]
        self.heap = MinBinaryHeap(self.keys, self.values)

    def insert(self):
        self.heap.insert(1, "a")

    def pop(self):
        self.heap.pop()

    def test_ensure_on_min_heap(self):
        heap = MinBinaryHeap(self.keys, self.values)
        self.assertEqual(self.heap._keys, [None] + self.keys)
        self.assertEqual(self.heap._values, [None] + self.values)

    def test_ensure_on_improper_min_heap(self):
        heap = MinBinaryHeap([3,2,4], ["d", "b", "c"])
        self.assertEqual(self.heap._keys, [None] + self.keys)
        self.assertEqual(self.heap._values, [None] + self.values)

    def test_insert(self):
        self.insert()
        self.assertEqual(self.heap._keys, [None, 1,2,4,3])
        self.assertEqual(self.heap._values, [None, "a", "b", "c", "d"])

    def test_pop(self):
        self.insert()
        self.assertEqual(self.heap._keys, [None, 1,2,4,3])
        self.assertEqual(self.heap._values, [None, "a", "b", "c", "d"])

        self.pop()
        self.assertEqual(self.heap._keys, [None, 2, 3, 4])
        self.assertEqual(self.heap._values, [None, "b", "d", "c"])

class TestMaxBinaryHeap(unittest.TestCase):
    def build_heap_from_array(self, array):
        heap = MaxBinaryHeap()
        for d in array:
            heap.insert(d)
        return heap

    def assert_maxheap_pop(self, heap, old_array):
        output = []
        while heap.get_size():
            output.append(heap.pop())

        self.assertEqual(output, 
            sorted(old_array, reverse=True))

    def test_pop(self):
        unsorted_data = [1, 3, 4, 5, 6, 6, 8, 2, 7]
        heap = self.build_heap_from_array(unsorted_data)

        self.assert_maxheap_pop(heap, unsorted_data)

    def test_size_after_insert(self):
        heap = MaxBinaryHeap()
        heap.insert(1)
        self.assertEqual(heap.get_size(), 1)

    def test_size_after_pop(self):
        heap = MaxBinaryHeap()
        heap.insert(1)
        heap.insert(2)
        self.assertEqual(heap.get_size(), 2)

        heap.pop()
        self.assertEqual(heap.get_size(), 1)

    def test_random_insert_pop(self):
        random_data = [random.randrange(1, 100) for _ in range(50)]
        heap = self.build_heap_from_array(random_data)
        self.assert_maxheap_pop(heap, random_data)

if __name__ == "__main__":
    unittest.main()
