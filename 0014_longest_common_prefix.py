from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = ""
        if len(strs) == 0:
            return commonPrefix

        minLength = min([len(item) for item in strs])
        for i in range(minLength):
            if all([item[i] == strs[0][i] for item in strs]):
                commonPrefix += strs[0][i]
            else:
                break

        return commonPrefix


if __name__ == '__main__':
    solution = Solution()
    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert solution.longestCommonPrefix([]) == ""

    """
    注意：edge case，空字符串数组。
    """
