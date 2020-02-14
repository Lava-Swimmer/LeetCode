class Solution:
    cachedResults = dict()

    def __init__(self):
        # 预先缓存数据，直接打表
        for i in range(1, 21):
            self.cachedResults[i] = self.climbStairs(i)

    def climbStairs(self, n: int) -> int:
        cache = self.cachedResults.get(n)
        if cache:
            return cache

        if n > 2:
            result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        elif n == 2:
            result = 2
        else:
            result = 1
        self.cachedResults[n] = result
        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.climbStairs(2) == 2
    assert solution.climbStairs(3) == 3
