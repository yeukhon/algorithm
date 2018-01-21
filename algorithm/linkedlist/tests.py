import unittest
from algorithm.linkedlist.linkedlist import SListNode, SLinkedList

class TestSLinkedListClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.node1 = SListNode(item=1)
        cls.node2 = SListNode(item=2)
        cls.node3 = SListNode(item=3)
        cls.node4 = SListNode(item=4)

    def create_ll(self):
        return SLinkedList()

    def create_node(self, v=None):
        return SListNode(item=v)

    def test_empty_list(self):
        ll = self.create_ll()
        self.assertEqual(ll.get_head_node(), None)
        self.assertEqual(ll.get_end_node(), None)
        self.assertEqual(ll.get_size(), 0)

    def test_one_node_list(self):
        ll = self.create_ll()
        ll.set_head_node(self.node1)
        self.assertEqual(ll.get_head_node(), self.node1)
        self.assertEqual(ll.get_end_node(), self.node1)
        self.assertEqual(ll.get_size(), 1)

    def test_add_new_head(self):
        ll = self.create_ll()
        ll.set_head_node(self.node1)
        ll.set_head_node(self.node2)
        self.assertEqual(ll.get_head_node(), self.node2)
        self.assertEqual(ll.get_end_node(), self.node1)
        self.assertEqual(ll.get_size(), 2)

    def test_slinkedlist_generator(self):
        ll = self.create_ll()
        ll.set_head_node(self.node1)
        ll.set_head_node(self.node2)
        self.assertEqual(
            [node for node in ll],
            [self.node2, self.node1]
        )

    def test_find_key_in_slinkedlist(self):
        ll = self.create_ll()
        ll.set_head_node(self.node1)
        ll.set_head_node(self.node2)
        self.assertEqual(ll.find(1), self.node1)
        self.assertEqual(ll.find(2), self.node2)
        self.assertEqual(ll.find(3), None)
