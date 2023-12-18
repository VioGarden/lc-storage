def isPalindrome(s):
    left, right = 0, len(s)-1 # to traverse, initialize index of both sides
    while left < right:  # while left index less than right index (want to end when meet at halfway point)
        if not isAlphaNum(s[left]): # if not alphanumeric
            left += 1 # increment to next element
            continue # goes to next iteration for while loop
        if not isAlphaNum(s[right]): # if not alphanumeric
            right -= 1 # decrement to next element
            continue # goes to next iteration for while loop
        if s[left].lower() != s[right].lower(): # if opposite elements do not match each other
            return False # return false
        left, right = left + 1, right - 1 # incremenet variables
    return True
    
def isAlphaNum(c): # function for testing if a character is alphabet
    return (
        ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9')
    )

def isAlphaNum2(c): # also valid way to check alpha num
    return (
        "a" <= c.lower() <= "z" or 
        "0" <= c.lower() <= "9"
    )