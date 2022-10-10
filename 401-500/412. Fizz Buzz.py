class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        i = 1
        final = []
        while i < n + 1:
            if i % 3 == 0 and i % 5 == 0:
                final.append("FizzBuzz")
            elif i % 3 == 0:
                final.append("Fizz")
            elif i % 5 == 0:
                final.append("Buzz")
            else:
                final.append(str(i))
            i += 1
        return final