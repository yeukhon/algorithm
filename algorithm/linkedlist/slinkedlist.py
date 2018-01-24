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

    def __repr__(self):
        return "{}('item={}, child={}, parent={}'}".format(
            self.__class__.__name__,
            self._item, self._next, self._parent)

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
            old_head.set_parent(new_head_node)
            self._head = new_head_node
            #note: the end node is still the old head

        self._increment_size()

    def set_end_node(self, new_last_node):
        """Insert the specific node to the end of the list."""

        old_end_node = self.get_end_node()
        if old_end_node:
            # okay, there is at least one node in this list
            old_end_node.set_child(new_last_node)

        self._increment_size()

    def append(self, new_node):
        end_node = self.get_end_node()
        if not end_node:
            self.set_head_node(new_node)
        else:
            end_node.set_child(new_node)
            new_node.set_parent(end_node)

        self._increment_size()

    def _remove(self, node):
        """Link specific node's parent and node's child so reference
        to node is removed from the list.

        """
        child = node.child()
        if child:
            node.parent().set_child(child)
            child.set_parent(node.parent())
            self._decrement_size()

    def remove(self, node=None, index=None, key=None):
        # link specific node's parent and node's child
        if node:
            self._remove(node)
        elif index is not None:
            # we still assume linked list follows zero-based indexing
            # so the index must be less than the actual size of the list.
            if index >= self.get_size():
                raise IndexError("Index exceeds the size of the linked list.")
            else:
                curr_node = self._head
                for i in range(0, index + 1):
                    curr_node = curr_node.child()
                self._remove(curr_node)
        else:
            # find the first node with this key, and remove it.
            _node = self.find(key)
            self._remove(_node)

    def find(self, key):
        """Find a list node by the node's key. If no match found,
        ``None`` is returned.

        """

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

    def _decrement_size(self):
        self._size -= 1

    def __iter__(self):
        curr_node = self.get_head_node()
        while curr_node:
            yield curr_node
            curr_node = curr_node.child()

    def __repr__(self):
        return "{}('head={}, end={}, size={}')".format(self.__class__.__name__,
            self._head, self._end, self._size)
