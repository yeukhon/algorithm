import unittest

from leetcode.s2_add_two_numbers import Solution, ListNode

class TestAddTwoNumbers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution().addTwoNumbers

    def test_default_case(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        answer = self.solution(l1, l2)
        self.assertEqual(answer.val, '7')
        self.assertEqual(answer.next.val, '0')
        self.assertEqual(answer.next.next.val, '8')

    def test_10_plus_20(self):
        l1 = ListNode(0)
        l1.next = ListNode(1)

        l2 = ListNode(0)
        l2.next = ListNode(2)

        answer = self.solution(l1, l2)
        self.assertEqual(answer.val, '0')
        self.assertEqual(answer.next.val, '3')

    def test_99_plus_1(self):
        l1 = ListNode(9)
        l1.next = ListNode(9)

        l2 = ListNode(1)

        answer = self.solution(l1, l2)
        self.assertEqual(answer.val, '0')
        self.assertEqual(answer.next.val, '0')
        self.assertEqual(answer.next.next.val, '1')

if __name__ == '__main__':
    unittest.main()
