from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        nums = set(arr)
        count = len([item for item in arr if item + 1 in nums])
        return count


if __name__ == '__main__':
    solution = Solution()
    assert solution.countElements([1, 2, 3]) == 2
    assert solution.countElements([1, 1, 3, 3, 5, 5, 7, 7]) == 0
    assert solution.countElements([1, 3, 2, 3, 5, 0]) == 3
    assert solution.countElements([1, 1, 2, 2]) == 2
