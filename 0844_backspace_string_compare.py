class Solution:
    def calculate(self, string: str) -> str:
        stack = []
        for char in string:
            if char == '#':
                if len(stack) >= 1:
                    stack.pop()
            else:
                stack.append(char)
        return str(stack)

    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.calculate(S) == self.calculate(T)


if __name__ == '__main__':
    solution = Solution()
    assert solution.backspaceCompare('ab#c', 'ad#c') is True
    assert solution.backspaceCompare('ab##', 'c#d#') is True
    assert solution.backspaceCompare('a##c', '#a#c') is True
    assert solution.backspaceCompare('a#c', 'b') is False
    assert solution.backspaceCompare('y#fo##f', 'y#f#o##f') is True
