# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain
# a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 140ms - brute force
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = ""
        s2 = ""
        i = l1
        while i:
            s1 += str(i.val)
            i = i.next

        j = l2
        while j:
            s2 += str(j.val)
            j = j.next

        s1 = "".join(reversed(s1))
        s2 = "".join(reversed(s2))
        total = int(s1) + int(s2)
        output_s = "".join(reversed(str(total)))
        start = ListNode(output_s[0])
        l3 = start
        for s in output_s[1:]:
            l3.next = ListNode(s)
            l3 = l3.next
        return start

    def get_sum(self, a, b, prev_carry):
        total = a + b + prev_carry
        if total >= 10:
            new_carry, c_val = 1, total - 10
        else:
            new_carry, c_val = 0, total
        return new_carry, ListNode(c_val)

    # 68ms 
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = l1
        b = l2
        carry, c = self.get_sum(a.val, b.val, 0)
        a = a.next
        b = b.next
        c_head = c
        while True:
            if a and b:
                carry, c.next = self.get_sum(a.val, b.val, carry)
                c = c.next
                a = a.next
                b = b.next
            elif a:
                while a:
                    carry, c.next = self.get_sum(a.val, 0, carry)
                    a = a.next
                    c = c.next
            elif b:
                while b:
                    carry, c.next = self.get_sum(b.val, 0, carry)
                    b = b.next
                    c = c.next
            else:
                break
        if carry == 1:
            c.next = ListNode(1)
        return c_head
