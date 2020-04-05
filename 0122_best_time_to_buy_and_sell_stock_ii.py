from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum([prices[i + 1] - prices[i] for i in range(len(prices) - 1) if prices[i + 1] - prices[i] > 0])


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert solution.maxProfit([1, 2, 3, 4, 5]) == 4
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
    assert solution.maxProfit([]) == 0
