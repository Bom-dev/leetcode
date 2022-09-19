class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        str = ''
        for letter in s:
            if letter not in str:
                str += letter
            else:
                str = str[str.index(letter) + 1:] + letter
            i = max(i, len(str))
        return i
