import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        s = re.sub('[^A-Za-z0-9]+', '', s)
        s = s.lower()
        reverse = s[::-1]
        if s == reverse:
            return True
        else:
            return False
