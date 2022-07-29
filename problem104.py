#c.f. problem 110
# NOTE: Binary tree isn't necessarily balanced!

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #67ms, 42.15% 
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        return self.isBalancedWithHeight(root)[1]
    
    def isBalancedWithHeight(self, root):
        if not root:
            return True, 0
        
        ltrue, lheight = self.isBalancedWithHeight(root.left)
        #if not ltrue: return False, 0

        rtrue, rheight = self.isBalancedWithHeight(root.right)
        #if not rtrue: return False, 0
        
        #if abs(rheight - lheight) > 1 : return False, 0
        
        return True, max(lheight, rheight) + 1
    
    #62ms, 52.31%
    # and there's another gaussian aronud a (10%) lower memory, so there is a simpler solution
    # oh, right, not *simpler*, but using a queue instead of recursion, obviously
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        lheight = self.maxDepth(root.left)
        rheight = self.maxDepth(root.right)
        return max(lheight, rheight) + 1