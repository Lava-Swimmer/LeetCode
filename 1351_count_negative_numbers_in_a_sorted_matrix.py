from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if n == 0:
            return 0

        eachRowFirstNegativeColumnIndexes = [n] * m
        result = 0
        for rindex, row in enumerate(grid):
            if row[0] < 0:
                result += ((m - rindex) * n)
                break
            for cindex, item in enumerate(row):
                if rindex > 0 and cindex >= eachRowFirstNegativeColumnIndexes[rindex - 1]:
                    result += (n - eachRowFirstNegativeColumnIndexes[rindex - 1])
                    break
                if item < 0:
                    result += (n - cindex)
                    break
        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]) == 8
    assert solution.countNegatives([[3, 2], [1, 0]]) == 0
    assert solution.countNegatives([[]]) == 0
