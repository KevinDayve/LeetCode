class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skip = s[l+1:r+1]
                skip2 = s[l:r] 
                return (skip == skip[::-1] or skip2 == skip2[::-1])
            l = l + 1
            r = r - 1
        return True
