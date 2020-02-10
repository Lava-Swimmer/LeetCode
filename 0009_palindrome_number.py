class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        last_half = 0
        while x > last_half:
            last_half = last_half * 10 + x % 10
            x = x // 10

        return x == last_half or x == last_half // 10


if __name__ == '__main__':
    solution = Solution()
    assert solution.isPalindrome(1221) == True
    assert solution.isPalindrome(121) == True
    assert solution.isPalindrome(-121) == False
    assert solution.isPalindrome(10) == False

    """
    注意：不转换为字符串地思路，为避免超出32位整型地范围，只转换后半段为逆序进行比较。
    其中，负数或者除0以外所有尾数为0的数字都不是回文。
    通过%10和//10计算可以取得每轮x的尾数和去掉尾数之后的数字。
    当x<last_half时，已经计算完后半段逆序数字。
    当x的位数为偶数时，前半段和后半段逆序相等；当x的位数为奇数时，前半段和后半段逆序的前n-1位相等。
    """