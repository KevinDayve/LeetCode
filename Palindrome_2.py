#Palindrome algo without using any fancy functions.
def Palindrome(string):
    string.lower()
    start = 0
    end = len(string) - 1

    for i in range(len(string)):
        if string[i] == string[end]:
            start += 1    #incrementing the start value
            end -= 1      #decrementing the end value.
        else:
            return False
        
    return True

print(Palindrome("aba"))
#Should return True.
