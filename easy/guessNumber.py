# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        low = 0
        high = n
        while low <= high:    
            mid = (low+high)//2
            result = guess(mid)
            if result == 0:
                return mid
            if result < 0 :
                high = mid-1
            if result > 0:
                low = mid+1
