from typing import List


class TreeNode:
    def __init__(self, value, depth, leftCount, rightCount):
        self.value = value
        self.depth = depth
        self.leftCount = leftCount
        self.rightCount = rightCount
        self.left = None
        self.right = None


class Solution:
    results = []

    def addNode(self, node: TreeNode):
        if node is None or node.depth > self.maxDepth:
            return

        if node.depth == self.maxDepth:
            self.results.append(node.value)

        if node.leftCount < self.pair:
            treeNode = TreeNode(f'{node.value}(', node.depth + 1, node.leftCount + 1, node.rightCount)
            node.left = treeNode
        if node.rightCount < self.pair and node.leftCount > node.rightCount:
            treeNode = TreeNode(f'{node.value})', node.depth + 1, node.leftCount, node.rightCount + 1)
            node.right = treeNode

        self.addNode(node.left)
        self.addNode(node.right)

    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return [""]

        self.results = []
        self.pair = n
        self.maxDepth = n * 2
        root = TreeNode('(', 1, 1, 0)
        self.addNode(root)
        return self.results


if __name__ == '__main__':
    solution = Solution()
    assert solution.generateParenthesis(3) == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    ]
    print(solution.generateParenthesis(0))
