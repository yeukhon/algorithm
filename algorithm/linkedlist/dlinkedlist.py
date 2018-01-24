# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import sys
if sys.version_info[0] < 3:
    range = xrange

class SListNode(object):
    def __init__(self, item=None):
        self._item = item
        self._previous = None
        self._next = None

    def previous(self):
        
    def parent(self):
        return self._parent

    def set_parent(self, parent_node):
        self._parent = parent_node

    def child(self):
        return self._next

    def set_child(self, child_node):
        self._next = child_node

    def get_item(self):
        return self._item

class DLinkedList(object):
    """Doubly linked list with a sentinel node.

    The sentinel node (T-node) is a DListNode whose 'item' field
    is set to None. T-node has reference to the start and the
    end of the doubly linked list. Here's the sketch:

    """

    def __init__(self):
        self._sentinel_node = DListNode()
        self._head = self._sentinel_node
        self._end = self._sentinel_node
        self._size = 0

    def set_head_node(self, new_head_node):
        """Insert the specific node to the front of the list.

        The head node refers to the "child" node in the sentinel
        node.

        """

        old_head = self.get_head_node()
        # the list is empty, first node is both head and end
        if not old_head:
            self._head.set_child(new_head_node)
            self._end.set_parent(new_head_node)
        else:
            # there's already a head, reset head, set old head's
            # parent to this new head, and new head's child
            # is old head.
            old_head._parent = new_head_node
            new_head_node._set_child(old_head)
            self._sentinel_node.set_child(new_head_node)

        self._increment_size()

    def set_end_node(self, new_last_node):
        """Insert the specific node to the end of the list."""

        old_end_node = self.get_end_node()
        if old_end_node:
            # okay, there is at least one node in this list
            old_end_node.set_child(new_last_node)

        self._increment_size()

    def find(self, key):
        next_node = self._head
        while next_node:
            if next_node.get_item() == key:
                return next_node
            else:
                next_node = next_node.child()

    def get_head_node(self):
        return self._head

    def get_end_node(self):
        return self._end

    def get_size(self):
        return self._size

    def _increment_size(self):
        self._size += 1

    def __iter__(self):
        curr_node = self.get_head_node()
        while curr_node:
            yield curr_node
            curr_node = curr_node.child()
