# Definition for singly-linked list.
from typing import List, Tuple


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getValueAndCarry(self, nums: List[int]) -> Tuple[int, int]:
        currentSum = sum(nums)
        if currentSum >= 10:
            value = currentSum % 10
            carry = currentSum // 10
        else:
            value = currentSum
            carry = 0
        return value, carry

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        p3 = l3 = ListNode(0)
        carry = 0
        while p1 and p2:
            value, carry = self.getValueAndCarry([p1.val, p2.val, carry])
            p3.next = ListNode(value)
            p1 = p1.next
            p2 = p2.next
            p3 = p3.next

        if p1:
            if carry == 0:
                p3.next = p1
            else:
                while p1:
                    value, carry = self.getValueAndCarry([p1.val, carry])
                    p3.next = ListNode(value)
                    p1 = p1.next
                    p3 = p3.next
        if p2:
            if carry == 0:
                p3.next = p2
            else:
                while p2:
                    value, carry = self.getValueAndCarry([p2.val, carry])
                    p3.next = ListNode(value)
                    p2 = p2.next
                    p3 = p3.next
        if carry:
            p3.next = ListNode(carry)
            p3 = p3.next

        return l3.next

    def calculate(self, nums1: List[int], nums2: List[int]):
        p1 = l1 = ListNode(0)
        p2 = l2 = ListNode(0)

        for num in nums1:
            p1.next = ListNode(num)
            p1 = p1.next
        for num in nums2:
            p2.next = ListNode(num)
            p2 = p2.next

        l3 = self.addTwoNumbers(l1.next, l2.next)
        p3 = l3

        int1 = int(''.join([str(num) for num in nums1[::-1]]))
        int2 = int(''.join([str(num) for num in nums2[::-1]]))
        int3 = int1 + int2
        target = [int(num) for num in str(int3)[::-1]]
        result = []
        while p3:
            result.append(p3.val)
            p3 = p3.next

        assert target == result


if __name__ == '__main__':
    solution = Solution()
    solution.calculate([2, 4, 3], [5, 6, 4])
    solution.calculate([1, 9, 9, 9], [9])
    solution.calculate([1, 9, 9, 9, 1], [9])
    solution.calculate([1, 9, 9, 9, 1], [0])
    solution.calculate([0], [1, 9, 9, 9, 1])
