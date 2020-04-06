from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for item in strs:
            groups.setdefault(''.join(sorted(list(item))), []).append(item)
        return list(groups.values())


if __name__ == '__main__':
    solution = Solution()
    assert solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ['eat', 'tea', 'ate'],
        ['tan', 'nat'],
        ['bat']
    ]
    assert solution.groupAnagrams(
        ["hos", "boo", "nay", "deb", "wow", "bop", "bob", "brr", "hey", "rye", "eve", "elf", "pup", "bum", "iva", "lyx",
         "yap", "ugh", "hem", "rod", "aha", "nam", "gap", "yea", "doc", "pen", "job", "dis", "max", "oho", "jed", "lye",
         "ram", "pup", "qua", "ugh", "mir", "nap", "deb", "hog", "let", "gym", "bye", "lon", "aft", "eel", "sol",
         "jab"]
    ) == [
               ['hos'], ['boo'], ['nay'], ['deb', 'deb'], ['wow'], ['bop'], ['bob'], ['brr'], ['hey'], ['rye'], ['eve'],
               ['elf'], ['pup', 'pup'], ['bum'], ['iva'], ['lyx'], ['yap'], ['ugh', 'ugh'], ['hem'], ['rod'], ['aha'],
               ['nam'], ['gap'], ['yea'], ['doc'], ['pen'], ['job'], ['dis'], ['max'], ['oho'], ['jed'], ['lye'],
               ['ram'],
               ['qua'], ['mir'], ['nap'], ['hog'], ['let'], ['gym'], ['bye'], ['lon'], ['aft'], ['eel'], ['sol'],
               ['jab']
           ]
