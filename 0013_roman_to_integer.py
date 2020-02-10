class Solution:
    symbols = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        sum = 0
        length = len(s)
        for i in range(length - 1):
            currentValue = self.symbols[s[i]]
            nextValue = self.symbols[s[i + 1]]
            if currentValue < nextValue:
                sum -= currentValue
            else:
                sum += currentValue
        sum += self.symbols[s[length - 1]]
        return sum


if __name__ == '__main__':
    solution = Solution()
    assert solution.romanToInt('III') == 3
    assert solution.romanToInt('IV') == 4
    assert solution.romanToInt('IX') == 9
    assert solution.romanToInt('LVIII') == 58
    assert solution.romanToInt('MCMXCIV') == 1994
    assert solution.romanToInt('MMMCMXCIX') == 3999

    """
    注意：比较前后两个数字，若前一个小于后一个，前一个数字需被减去，否则为加。
    """
