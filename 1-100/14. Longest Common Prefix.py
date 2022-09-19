class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:  # O(n + m) time
        if len(strs) == 0:
            return ""
        i, x, y = 0, min(strs), max(strs)
        while i < min(len(x), len(y)) and x[i] == y[i]:
            i += 1
        return x[:i]
