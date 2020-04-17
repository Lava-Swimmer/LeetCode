from typing import List


class Solution:
    ratio = {0: 1, 1: -1}

    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for direction, amount in shift:
            amount *= self.ratio.get(direction)
            s = s[amount:] + s[:amount]
        return s


if __name__ == '__main__':
    solution = Solution()
    assert solution.stringShift('abc', [[0, 1], [1, 2]]) == 'cab'
    assert solution.stringShift('abcdefg', [[1, 1], [1, 1], [0, 2], [1, 3]]) == 'efgabcd'
