class Solution(object):
    def hammingWeight(self, n):
        binary = bin(n)[2:]
        binary = str(binary)
        count = 0
        for i in range(len(binary)):
            if binary[i]=='1':
                count+=1
        return count
