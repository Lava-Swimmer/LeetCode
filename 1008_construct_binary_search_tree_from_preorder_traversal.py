from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(lower: TreeNode, upper: TreeNode, preorder: deque) -> TreeNode:
            if preorder:
                root = None
                if upper.val > preorder[0] > lower.val:
                    root = TreeNode(preorder[0])
                    preorder.popleft()
                    root.left = helper(lower, root, preorder)
                    root.right = helper(root, upper, preorder)
                return root
            else:
                return

        return helper(TreeNode(float('-inf')), TreeNode(float('inf')), deque(preorder))

    def test(self, preorder: List[int]):
        binary_order = []
        root = self.bstFromPreorder(preorder)
        Q = deque()
        Q.append(root)
        while len(Q) > 0:
            node = Q.popleft()
            binary_order.append(node.val if node else None)
            if node and (node.left or node.right):
                Q.append(node.left)
                Q.append(node.right)

        return binary_order


if __name__ == '__main__':
    solution = Solution()
    assert solution.test([8, 5, 1, 7, 10, 12]) == [8, 5, 10, 1, 7, None, 12]
