# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return
        if head.next is None:
            return head

        p1 = head
        p2 = p1.next
        while p2:
            if p2.val == p1.val:
                p2 = p2.next
            else:
                p1.next = p2
                p1 = p1.next

        p1.next = p2
        return head

    def calculate(self, nums: List[int]):
        l1 = ListNode(0)
        p1 = l1
        for num in nums:
            p1.next = ListNode(num)
            p1 = p1.next

        target = sorted(set(nums))
        result = []
        l2 = self.deleteDuplicates(l1.next)
        p2 = l2
        while p2:
            result.append(p2.val)
            p2 = p2.next

        assert target == result


if __name__ == '__main__':
    solution = Solution()
    solution.calculate([1, 1, 2])
    solution.calculate([1, 1, 2, 3, 3])
    solution.calculate([1, 1, 2, 3, 3, 4])
    solution.calculate([1])
    solution.calculate([1, 1, 1])
    solution.calculate([])
