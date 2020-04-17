from typing import List


def bfs(grid: List[List[str]], i: int, j: int):
    deq = []
    deq.append([i, j])
    while deq:
        x, y = deq.pop()
        grid[x][y] = 'v'  # visited
        if x + 1 < len(grid) and grid[x + 1][y] == '1':
            deq.append([x + 1, y])
        if y + 1 < len(grid[0]) and grid[x][y + 1] == '1':
            deq.append([x, y + 1])
        if y - 1 >= 0 and grid[x][y - 1] == '1':
            deq.append([x, y - 1])
        if x - 1 >= 0 and grid[x - 1][y] == '1':
            deq.append([x - 1, y])


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(grid, i, j)
                    count += 1
        return count


def test(s: str, count: int):
    grid = [[char for char in line.strip()] for line in s.split('\n') if len(line.strip()) > 0]
    assert solution.numIslands(grid) == count


if __name__ == '__main__':
    solution = Solution()
    s = """
    11110
    11010
    11000
    00000
    """
    test(s, 1)
    s = """
    11000
    11000
    00100
    00011
    """
    test(s, 3)
