class Solution:
    def isHappy(self, n: int) -> bool:
        p = (n == 1) + (n == 7) + (n < 10)
        if p == 2:
            return True
        if p == 0:
            return self.isHappy(sum(int(x) ** 2 for x in str(n)))
        else:
            return False
        return self.isHappy(n)