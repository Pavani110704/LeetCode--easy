class Solution(object):
    def reverseVowels(self, s):
        vowels = set('aeiouAEIOU')
        s = list(s)  # convert to list for in-place edits
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1

            # swap vowels
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)
