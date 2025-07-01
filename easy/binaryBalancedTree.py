# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        def check(node):
            if not node:
                return True, 0
            
            left_balanced, left_height = check(node.left)
            right_balanced, right_height = check(node.right)
            
            balanced = (
                left_balanced and 
                right_balanced and 
                abs(left_height - right_height) <= 1
            )
            
            height = 1 + max(left_height, right_height)
            return balanced, height
        
        balanced, _ = check(root)
        return balanced
