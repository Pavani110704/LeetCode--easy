# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution(object):
    def firstBadVersion(self, n):
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid  # first bad version is at mid or before
            else:
                left = mid + 1  # first bad version must be after mid

        return left  # or return right, both are same when loop ends
