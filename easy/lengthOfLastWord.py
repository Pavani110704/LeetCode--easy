class Solution(object):
    def lengthOfLastWord(self, s):
        result = s.split()
        length =  result[-1]
        return len(length)
