class Solution:
    used_nums = []

    def isHappy(self, n: int) -> bool:
        self.used_nums.append(n)

        if n == 1:
            self.used_nums = []
            return True

        temp = n
        nums = []
        while temp > 0:
            num = temp % 10
            nums.append(num)
            temp = temp // 10

        value = sum(map(lambda x: x ** 2, nums))

        if value == n or value in self.used_nums:
            self.used_nums = []
            return False

        return self.isHappy(value)


if __name__ == '__main__':
    solution = Solution()
    # assert solution.isHappy(19) is True
    # assert solution.isHappy(20) is False
    assert solution.isHappy(7) is True
