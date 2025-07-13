class Solution(object):
    def moveZeroes(self, nums):
        last_non_zero = 0

        # Move all non-zero elements to the beginning
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero] = nums[i]
                last_non_zero += 1

        # Fill remaining positions with zero
        for i in range(last_non_zero, len(nums)):
            nums[i] = 0
