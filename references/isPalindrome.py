def isPalindrome(str):
    strat_index = 0
    end_index = len(str) - 1
    
    for i in str:
        if str[strat_index] != str[end_index]:
            return False
    return True