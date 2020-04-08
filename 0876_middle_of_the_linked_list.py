# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        p1 = head
        p2 = head
        while True:
            if p2 is None or p2.next is None:
                return p1
            else:
                p1 = p1.next
                p2 = p2.next.next

    def run(self, nums: List[int]) -> ListNode:
        head = ListNode(nums[0])
        p = head
        for num in nums[1:]:
            node = ListNode(num)
            p.next = node
            p = p.next

        return self.middleNode(head)


if __name__ == '__main__':
    solution = Solution()
    assert solution.run([1, 2, 3, 4, 5]).val == 3
    assert solution.run([1, 2, 3, 4, 5, 6]).val == 4
