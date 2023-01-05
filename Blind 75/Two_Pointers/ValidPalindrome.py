def isalnum(c):
    return ( (ord('0') <= ord(c) <= ord('9')) or
                (ord('a') <= ord(c) <= ord('z'))
            ) 
def isPalindrome(s):
    leftIndex, rightIndex = 0, len(s) - 1
    
    while leftIndex < rightIndex:
        while leftIndex < rightIndex and not isalnum(s[leftIndex].lower()):
            leftIndex += 1
        while rightIndex > leftIndex and not isalnum(s[rightIndex].lower()):
            rightIndex -= 1
        if(s[leftIndex].lower() == s[rightIndex].lower()):
            leftIndex += 1
            rightIndex -= 1
        else:
            return False
    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))