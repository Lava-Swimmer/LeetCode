from typing import List


class Solution:
    numberLetterDict = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits: str) -> List[str]:
        results = None
        for digit in digits:
            letters = self.numberLetterDict[digit]
            if not results:
                results = letters
            else:
                results = [f'{a}{b}' for a in results for b in letters]
        return results


if __name__ == '__main__':
    solution = Solution()
    assert solution.letterCombinations('23') == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert solution.letterCombinations('345') == ["dgj", "dgk", "dgl", "dhj", "dhk", "dhl", "dij", "dik", "dil", "egj",
                                                  "egk", "egl", "ehj", "ehk", "ehl", "eij", "eik", "eil", "fgj", "fgk",
                                                  "fgl", "fhj", "fhk", "fhl", "fij", "fik", "fil"]
