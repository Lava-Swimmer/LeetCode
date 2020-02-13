from typing import List


class Solution:
    def sumChars(self, chars: List[str]) -> int:
        return sum(int(char) for char in chars)

    def addBinary(self, a: str, b: str) -> str:
        c = ''
        aLength = len(a)
        bLength = len(b)
        if aLength > bLength:
            b = '0' * (aLength-bLength) + b
            bLength = len(b)
        elif bLength > aLength:
            a = '0' * (bLength-aLength) + a
            aLength = len(a)

        temp = '0'
        for i in range(aLength):
            aChar = a[aLength-i-1]
            bChar = b[bLength-i-1]
            charsSum = self.sumChars([aChar,bChar, temp])
            if charsSum % 2 == 0:
                value = '0'
            else:
                value = '1'
            if charsSum < 2:
                temp = '0'
            else:
                temp = '1'
            c = value + c
        if temp == '1':
            c = temp + c
        return c

if __name__ == '__main__':
    solution = Solution()
    assert solution.addBinary('11', '1') == '100'
    assert solution.addBinary('11', '11') == '110'
    assert solution.addBinary('1010', '1011') == '10101'
