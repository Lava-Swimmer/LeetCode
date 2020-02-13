class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len((s.rstrip().split(' ') or [''])[-1])


if __name__ == '__main__':
    solution = Solution()
    # assert solution.lengthOfLastWord('Hello World') == 5
    # assert solution.lengthOfLastWord('Hello') == 5
    # assert solution.lengthOfLastWord('') == 0
    assert solution.lengthOfLastWord('a ') == 1

    """
    注意：edge case: 'a '
    """