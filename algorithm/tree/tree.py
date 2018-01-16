# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import sys
if sys.version_info[0] < 3:
    range = xrange

class Tree(object):
    """
    A tree is defined as a set of nodes and edges that connected
    the nodes together. A rooted tree has one root, and have one
    or more children nodes.

    """

    def __init__(self):
        self.size = 0
        self.root = None

    def preorder_walk(self, do_print=False):
        return self.root.preorder_walk(do_print=do_print)

    def postorder_walk(self, do_print=False):
        return self.root.postorder_walk(do_print=do_print)

class TreeNode(object):
    """
    A tree node has a parent, a value, and may have one or more
    children and siblings.

    """

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.first_child = None
        self.next_sibling = None
        self.size = 0

    def set_parent(self, parent_node):
        self.parent = parent_node

    def set_first_child(self, first_child_node):
        self.first_child = first_child_node

    def set_next_sibling(self, sibling_node):
        self.next_sibling = sibling_node

    def visit(self, do_print=False):
        if do_print:
            print(self.value)

    def preorder_walk(self, do_print=False):
        """Preorder traversal works by:
        1. visit the node itself
        2. visit its first child recursively
        3. visit its next sibiling recursively

        """

        l = s = []
        self.visit(do_print=do_print)        

        if self.first_child is not None:
            l = self.first_child.preorder_walk(do_print=do_print)

        if self.next_sibling is not None:
            s = self.next_sibling.preorder_walk(do_print=do_print)

        return [self.value] + l + s

    def postorder_walk(self, do_print=False):
        """Postorder traversal works by:
        1. visit its first child recurisvely
        2. visit the node itself
        3. visit its next sibling recursively

        """

        l = s = []

        if self.first_child is not None:
            l = self.first_child.postorder_walk(do_print=do_print)

        self.visit(do_print=do_print)

        if self.next_sibling is not None:
            s = self.next_sibling.postorder_walk(do_print=do_print)

        return l + [self.value] + s
