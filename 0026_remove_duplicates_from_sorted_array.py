from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        temp = nums[0]
        for index, num in enumerate(nums[1:]):
            if num == temp:
                nums.remove(num)
            else:
                temp = num

        return len(nums)


if __name__ == '__main__':
    solution = Solution()
    assert solution.removeDuplicates([1, 1, 2]) == 2
    assert solution.removeDuplicates([]) == 0
    assert solution.removeDuplicates([1, 1, 1]) == 1
