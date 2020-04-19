from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) <= 0 or grid is None:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue
                if r - 1 < 0:  # 第一行
                    grid[r][c] = grid[r][c] + grid[r][c - 1]
                elif c - 1 < 0:  # 第一列
                    grid[r][c] = grid[r][c] + grid[r - 1][c]
                else:  # 其它
                    grid[r][c] = grid[r][c] + min(grid[r - 1][c], grid[r][c - 1])
        return grid[rows - 1][cols - 1]


if __name__ == '__main__':
    solution = Solution()
    assert solution.minPathSum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]) == 7
