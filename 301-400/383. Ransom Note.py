class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if Counter(ransomNote) & Counter(magazine) == Counter(ransomNote):
            return True
        else:
            return False
