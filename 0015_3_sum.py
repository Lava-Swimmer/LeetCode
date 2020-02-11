from collections import Counter
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        finds = sorted(counter.items(), key=lambda x: (x[0]))
        if counter[0] >= 3:
            results = {(0, 0, 0)}
        else:
            results = set()
        for i, (key1, value1) in enumerate(finds):
            if value1 >= 2 and -2 * key1 in counter and key1 != 0:
                if key1 < 0:
                    results.add((key1, key1, -2 * key1))
                else:
                    results.add((-2 * key1, key1, key1))
            for key2, value2 in finds[i + 1:]:
                if key1 + 2 * key2 >= 0:
                    break
                elif -(key1 + key2) in counter:
                    results.add((key1, key2, -key1 - key2))
        return [list(item) for item in results]


if __name__ == '__main__':
    solution = Solution()
    assert solution.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]]
    assert solution.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
    assert solution.threeSum([0, 0, 0]) == [[0, 0, 0]]
    assert solution.threeSum([0, 0]) == []
    assert solution.threeSum([-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]) == [[-4, 1, 3], [-2, 1, 1],
                                                                                           [0, 0, 0], [-2, -2, 4],
                                                                                           [-4, 0, 4], [-5, 1, 4]]
    """
    注意：edge case: [0,0,0,0]、[0,0,0]和[0,0]
    普通的思路使用三次for循环会超时
    """
