input = "anbbna"

# T: O(N) | S: O(1)
def check_palindrome(input):
    startIndex = 0
    endIndex = len(input) - 1

    while(startIndex < endIndex): # < means center odd char is not even evaluated , using it with even chars would allow for comparison and would work!
        if(input[startIndex] != input[endIndex]):
            return False
        startIndex += 1
        endIndex -= 1
    return True

print(check_palindrome(input))