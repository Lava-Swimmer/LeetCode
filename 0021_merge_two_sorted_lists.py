# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        p1 = l1
        p2 = l2
        p3 = l3
        while p1 and p2:
            if p1.val <= p2.val:
                value = p1.val
                p1 = p1.next
            else:
                value = p2.val
                p2 = p2.next
            p3.next = ListNode(value)
            p3 = p3.next

        while p1:
            p3.next = ListNode(p1.val)
            p3 = p3.next
            p1 = p1.next
        while p2:
            p3.next = ListNode(p2.val)
            p3 = p3.next
            p2 = p2.next

        return l3.next

    def calculate(self, list1: list, list2: list):
        l1, l2 = ListNode(0), ListNode(0)
        p1, p2 = l1, l2
        for item in list1:
            p1.next = ListNode(item)
            p1 = p1.next
        for item in list2:
            p2.next = ListNode(item)
            p2 = p2.next

        target = list(sorted([*list1, *list2]))
        result = []
        p3 = self.mergeTwoLists(l1.next, l2.next)
        while p3:
            result.append(p3.val)
            p3 = p3.next
        assert target == result


if __name__ == '__main__':
    solution = Solution()
    solution.calculate([1, 2, 4], [1, 3, 4])
