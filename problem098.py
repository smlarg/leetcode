# submitted
# feels janky, but it top 10% by speed (but 500kB above the median puts it in the bottom 15% by memomry)
# (I don't know that I trust these metrics)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_node(mr_node):
            if mr_node.left:
                left_true, left_min, left_max = check_node(mr_node.left)
                if not left_true:
                    return False, -1, -1
                if left_max >= mr_node.val:
                    return False, -1, -1
                my_min = left_min
            else:
                my_min = mr_node.val
            
            if mr_node.right:
                right_true, right_min, right_max = check_node(mr_node.right)
                if not right_true:
                    return False, -1, -1
                if right_min <= mr_node.val:
                    return False, -1, -1
                my_max = right_max
            else:
                my_max = mr_node.val
            
            return True, my_min, my_max
        
        return check_node(root)[0]
