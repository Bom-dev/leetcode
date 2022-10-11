def isPalindrome(str):
    start_index = 0
    end_index = len(str) - 1
    
    for i in str:
        if str[start_index] != str[end_index]:
            return False
        start_index += 1
        end_index -= 1
    return True