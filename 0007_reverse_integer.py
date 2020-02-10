class Solution:
    max = 2 ** 31 - 1
    min = -2 ** 31

    def reverse(self, x: int) -> int:
        positive = (x >= 0)
        reversed_int = int(str(abs(x))[::-1])
        if not positive:
            reversed_int = -1 * reversed_int
        if self.min <= reversed_int <= self.max:
            return reversed_int
        else:
            return 0


if __name__ == '__main__':
    solution = Solution()
    assert solution.reverse(123) == 321
    assert solution.reverse(-123) == -321
    assert solution.reverse(120) == 21
    assert solution.reverse(1534236469) == 0

    """
    注意：32位有符号整型的范围[-2^31, 2^31-1]
    """