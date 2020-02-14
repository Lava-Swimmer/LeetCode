from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = 0, 0
        while p2 < n:
            if p1 < m + p2:
                if nums2[p2] < nums1[p1]:
                    nums1.insert(p1, nums2[p2])
                    p2 += 1
                else:
                    p1 += 1
            else:
                nums1[p1] = nums2[p2]
                p2 += 1
                p1 += 1

        while len(nums1) > (m+n):
            nums1.pop()

        return nums1

if __name__ == '__main__':
    solution = Solution()
    assert solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]
    assert solution.merge([0],0,[1],1) == [1]
