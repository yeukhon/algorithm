import unittest

from heap import MinBinaryHeap
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

if __name__ == "__main__":
    unittest.main()
