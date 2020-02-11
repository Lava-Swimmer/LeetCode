# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next is None and n >= 1:
            return

        newHead = ListNode(0)
        p1, p2, p3 = head, head, newHead
        index = 0

        while p1.next:
            if index >= n - 1:
                p3.next = ListNode(p2.val)
                p2 = p2.next
                p3 = p3.next
            index += 1
            p1 = p1.next

        p3.next = p2.next
        return newHead.next

    def calculate(self, nums: List[int], n: int):
        head = None
        p = None
        for num in nums:
            node = ListNode(num)
            if head is None:
                head = node
                p = head
            else:
                p.next = node
                p = p.next

        target = []
        length = len(nums)
        for i, num in enumerate(nums):
            if i == length - n:
                continue
            target.append(num)

        newHead = self.removeNthFromEnd(head, n)
        newNums = []
        if newHead:
            p = newHead
            while p.next:
                newNums.append(p.val)
                p = p.next
            newNums.append(p.val)
        assert target == newNums


if __name__ == '__main__':
    solution = Solution()
    solution.calculate([1, 2, 3, 4, 5], 2)
    solution.calculate([1], 1)
    solution.calculate([1, 2], 2)

    """
    注意：快慢指针；去除的节点是第一个节点之类的边界条件。
    """