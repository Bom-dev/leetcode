# 1. Slice Function
# str[start:stop:step]
trial = 'reversal'
new_trial = trial[::-1]
print(new_trial) # output: lasrever


# 2. Recursion
def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]

str = 'reversal'
reverse = string_reverse(str)
print(reverse) # output: lasrever