from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        zero_length = 0
        i = 0
        while i < length - zero_length:
            if nums[i] == 0:
                del nums[i]
                zero_length += 1
                nums.append(0)
            else:
                i += 1


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]
    nums = [0, 0, 1]
    solution.moveZeroes(nums)
    assert nums == [1, 0, 0]
