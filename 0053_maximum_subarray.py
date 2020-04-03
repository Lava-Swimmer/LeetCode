from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxCurrent = nums[0]
        maxGlobal = nums[0]
        for num in nums[1:]:
            maxCurrent = max(num, maxCurrent + num)
            maxGlobal = max(maxCurrent, maxGlobal)
        return maxGlobal


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert solution.maxSubArray([-2, -1]) == -1
