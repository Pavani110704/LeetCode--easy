import re

class Solution(object):
    def isPalindrome(self, s):
        # Remove non-alphanumeric characters and convert to lowercase
        s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        
        # Two-pointer check
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
