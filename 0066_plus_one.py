from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
        else:
            length = len(digits)
            if length == 1:
                return [1, 0]
            else:
                digits[-1] = 0
                length = length - 2
                while length >= 0:
                    if digits[length] < 9:
                        digits[length] += 1
                        break
                    else:
                        digits[length] = 0
                        if length == 0:
                            digits.insert(0, 1)
                    length -= 1

        return digits


if __name__ == '__main__':
    solution = Solution()
    assert solution.plusOne([1, 2, 3]) == [1, 2, 4]
    assert solution.plusOne([9]) == [1, 0]
    assert solution.plusOne([9, 9]) == [1, 0, 0]
    assert solution.plusOne([1, 9, 9]) == [2, 0, 0]
    assert solution.plusOne([1, 9, 8, 9]) == [1, 9, 9, 0]
    assert solution.plusOne([1, 9, 8, 9, 8]) == [1, 9, 8, 9, 9]
