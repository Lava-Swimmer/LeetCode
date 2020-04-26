class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        matrix = [[0 for l in range(len(text1) + 1)] for l in range(len(text2) + 1)]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if text1[j - 1] == text2[i - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1] + 1
                else:
                    matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

        return matrix[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    assert solution.longestCommonSubsequence('abcde', 'ace') == 3
    assert solution.longestCommonSubsequence('abc', 'abc') == 3
    assert solution.longestCommonSubsequence('abc', 'def') == 0
