from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            max1 = max(stones)
            stones.remove(max1)
            max2 = max(stones)
            stones.remove(max2)
            value = abs(max2 - max1)
            if value != 0:
                stones.append(value)

        if len(stones) == 1:
            return stones[0]
        else:
            return 0


if __name__ == '__main__':
    solution = Solution()
    assert solution.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert solution.lastStoneWeight([]) == 0
    assert solution.lastStoneWeight([4]) == 4
