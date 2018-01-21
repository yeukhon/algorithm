# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import sys
if sys.version_info[0] < 3:
    range = xrange

class SListNode(object):
    def __init__(self, item=None):
        self._item = item
        self._next = None
        self._parent = None

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

class SLinkedList(object):

    def __init__(self):
        self._head = None
        self._end = None
        self._size = 0

    def set_head_node(self, new_head_node):
        """Insert the specific node to the front of the list."""

        old_head = self.get_head_node()
        if not old_head:
            self._head = new_head_node
            self._end = new_head_node
        else:
            old_head = self._head
            new_head_node.set_child(old_head)
            self._head = new_head_node

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
