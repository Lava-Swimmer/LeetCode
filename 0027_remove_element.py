from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)

        return len(nums)


if __name__ == '__main__':
    solution = Solution()
    assert solution.removeElement([3, 2, 2, 3], 3) == 2
    assert solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
    assert solution.removeElement([], 2) == 0
