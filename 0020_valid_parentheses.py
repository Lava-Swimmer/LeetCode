class Solution:
    pairs = {
        '(': -1,
        ')': 1,
        '[': -2,
        ']': 2,
        '{': -3,
        '}': 3

    }

    def isValid(self, s: str) -> bool:
        stack1 = list(s)
        stack2 = []
        if len(stack1) % 2 == 1:
            return False

        while len(stack1) >= 2:
            item1 = stack1.pop()
            item2 = stack1.pop()
            if self.pairs[item1] + self.pairs[item2] == 0 and self.pairs[item1] > 0 > self.pairs[item2]:
                stack1.extend(stack2)
                stack2 = []
            else:
                stack2.insert(0, item1)
                stack1.append(item2)
        return len(stack2) == 0


if __name__ == '__main__':
    solution = Solution()
    assert solution.isValid('()') == True
    assert solution.isValid('()[]{}') == True
    assert solution.isValid('{]') == False
    assert solution.isValid('([)]') == False
    assert solution.isValid('{[]}') == True
    assert solution.isValid('][') == False
    assert solution.isValid('[') == False

"""
注意：奇数个符号直接返回False
"""
