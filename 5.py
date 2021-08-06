# write a funtion that takes in a string as input and returns true if it is a palindrome, else returns false

def isPalindrome(s):
    x = (s == s[::-1])
 
    if x == True:
        print(True)
    else:
        print(False)
