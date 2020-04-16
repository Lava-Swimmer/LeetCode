from functools import reduce
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = reduce(lambda x, y: x * y, nums)
        results = []
        for index, num in enumerate(nums):
            if num == 0:
                result = reduce(lambda x, y: x * y, nums[:index] + nums[index + 1:])
            else:
                result = int(total / num)
            results.append(result)
        return results


if __name__ == '__main__':
    solution = Solution()
    assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
