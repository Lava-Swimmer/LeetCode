# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def depthOfNode(self, node: TreeNode):
        if node is None:
            return -1

        depth = max(self.depthOfNode(node.left), self.depthOfNode(node.right)) + 1

        return depth

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        diameter = max(
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right),
            self.depthOfNode(root.left) + self.depthOfNode(root.right) + 2
        )
        return diameter


if __name__ == '__main__':
    nodes = [TreeNode(i) for i in range(1, 6)]
    root = nodes[0]
    root.left = nodes[1]
    root.right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    solution = Solution()
    assert solution.diameterOfBinaryTree(root) == 3
