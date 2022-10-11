class Solution:
    def isPalindrome(self, s: str) -> bool:
        organized = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        start_index = 0
        end_index = len(organized) - 1
        for i in organized:
            if organized[start_index] != organized[end_index]:
                return False
            start_index += 1
            end_index -= 1
        return True