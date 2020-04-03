class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}
        while True:
            n = sum(int(d) ** 2 for d in str(n))
            if n == 1:
                return True
            elif n in seen:
                return False
            else:
                seen.add(n)


if __name__ == '__main__':
    solution = Solution()
    assert solution.isHappy(19) is True
    assert solution.isHappy(20) is False
    assert solution.isHappy(7) is True
