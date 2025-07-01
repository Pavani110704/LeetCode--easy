# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        # Base case: if the array is empty, return None
        if not nums:
            return None

        # Find the middle index
        mid = len(nums) // 2
        
        # Create the root node with the middle element
        root = TreeNode(nums[mid])
        
        # Recursively build the left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])       # Left half
        root.right = self.sortedArrayToBST(nums[mid+1:])    # Right half
        
        return root
