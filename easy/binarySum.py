class Solution(object):
    def addBinary(self, a, b):
        sums = int(a, 2) + int(b, 2)
        
        binary = bin(sums)[2:]
        return binary