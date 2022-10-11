class Solution:
    def reverse(self, x: int) -> int:
        stringfy = str(x)
        r_stringfy = stringfy[::-1]
        index = len(r_stringfy)
        if r_stringfy[index - 1] == '-':
            result = r_stringfy.replace('-', '')
            arrange = '-' + result
            return int(arrange) if -2147483648 <= int(arrange) <= 2147483647 else 0
        else:
            return int(r_stringfy) if -2147483648 <= int(r_stringfy) <= 2147483647 else 0