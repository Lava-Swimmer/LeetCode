class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s

        results = [''] * numRows
        results[0] = s[0]
        currentRow = 0
        plusRow = 1
        for char in s[1:]:
            currentRow += plusRow
            results[currentRow] += char
            if not 0 < currentRow < numRows - 1:
                plusRow *= -1

        return ''.join(results)


if __name__ == '__main__':
    """
    第一行：(正整数-1)*n
    第二行：(正整数-1)*(n-1
    """
    solution = Solution()
    assert solution.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    assert solution.convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
    assert solution.convert('P', 1) == 'P'
    assert solution.convert('PAYPALISHIRING', 20) == 'PAYPALISHIRING'
    assert solution.convert('AB', 1) == 'AB'