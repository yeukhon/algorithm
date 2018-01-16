import unittest
from algorithm.tree.tree import Tree, TreeNode

class TestTreeClass(unittest.TestCase):
    def get_tree(self):
        return Tree()

    def create_tree(self):
        tree = self.get_tree()
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)

        node1.set_first_child(node2)
        node2.set_first_child(node4)
        node2.set_next_sibling(node3)

        tree.root = node1
        return tree

    def test_empty_tree(self):
        tree = self.get_tree()
        self.assertEqual(tree.size, 0)
        self.assertEqual(tree.root, None)

    def test_preorder_walk(self):
        tree = self.create_tree()
        output = tree.preorder_walk(do_print=True)
        self.assertEqual(output, [1, 2, 4, 3])

    def test_postorder_walk(self):
        tree = self.create_tree()
        output = tree.postorder_walk(do_print=True)
        self.assertEqual(output, [4, 2, 3, 1])
