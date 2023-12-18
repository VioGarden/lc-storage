def isPalindrome(s):
    newStr = ""    # initialize empty string
    for i in s:    # for each 
        if i.isalnum(): # if element is alphanumbering
            newStr += i.lower() # append to string
    if newStr == newStr[::-1]: # if reverse equals regular
        return True # is true, palindrome
    return False # else, is false, not palindrome

print(isPalindrome("A man, a plan, a canal: Panama"))
# output : [1,2]