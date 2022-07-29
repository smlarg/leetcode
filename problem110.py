# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 73ms, 62.82%, good enough
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        return self.isBalancedWithHeight(root)[0]
    
    def isBalancedWithHeight(self, root):
        if not root:
            return True, 0
        
        ltrue, lheight = self.isBalancedWithHeight(root.left)
        if not ltrue: return False, 0

        rtrue, rheight = self.isBalancedWithHeight(root.right)
        if not rtrue: return False, 0
        
        if abs(rheight - lheight) > 1 : return False, 0
        
        return True, max(lheight, rheight) + 1