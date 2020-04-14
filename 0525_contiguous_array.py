from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        partial_sum = 0

        # table is a dictionary
        # key : partial sum value
        # value : the left-most index who has the partial sum value

        table = {0: -1}

        max_length = 0

        for idx, number in enumerate(nums):

            # partial_sum add 1 for 1
            # partial_sum minus 1 for 0

            if number:
                partial_sum += 1
            else:
                partial_sum -= 1

            if partial_sum in table:

                # we have a subarray with equal number of 0 and 1
                # update max length

                max_length = max(max_length, (idx - table[partial_sum]))

            else:
                # update the left-most index for specified partial sum value
                table[partial_sum] = idx

        return max_length


if __name__ == '__main__':
    solution = Solution()
    assert solution.findMaxLength([0, 1]) == 2
    assert solution.findMaxLength([0, 1, 0]) == 2
    assert solution.findMaxLength([0, 0, 0, 1, 1, 1, 0]) == 6
    assert solution.findMaxLength(
        [0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1,
         1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0,
         0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1]) == 68
