from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        count = 0
        for i in range(len(nums)):
            if count == 0:
                majority = nums[i]
                count = 1
            else:
                if nums[i] == majority:
                    count += 1
                else:
                    count -= 1
        if count > 0:
            return majority


if __name__ == '__main__':
    solution = Solution()
    assert solution.majorityElement([3, 2, 3]) == 3
    assert solution.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert solution.majorityElement([1, 2, 1, 2, 1, 2, 3, 2, 2]) == 2
