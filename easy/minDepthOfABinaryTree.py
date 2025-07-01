# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        
        # If left subtree is None, recurse only on right
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        # If right subtree is None, recurse only on left
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # If both children exist, take the min of both depths
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
