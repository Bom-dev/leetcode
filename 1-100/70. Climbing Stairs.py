class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        total, prev, prev2 = 0, 1, 2
        for _ in range(3, n + 1):
            total = prev2 + prev
            prev = prev2
            prev2 = total
        return total
