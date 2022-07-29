# Rank 1,029,876
# 15 medium, 50.9%

# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def treeFromArray(vals):

    from collections import deque
    valq = deque(vals)

    root = TreeNode(valq.popleft())
    nodeq = deque([root])

    while valq:
        node = nodeq.popleft()
        left = valq.popleft()
        if left:
            node.left = TreeNode(left)
            nodeq.append(node.left)
        right = valq.popleft()
        if right:
            node.right = TreeNode(right)
            nodeq.append(node.right)
    
    return root

vals = [3,9,20,None,None,15,7]

# 65ms, 24.77%, upper half of the gaussian (poison)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        
        q1, q2 = deque(), deque()
        
        if root: q1.append(root) # a bit hackish??
        
        result = []
        
        while q1 or q2:
            
            sub_result = []
            while q1:
                node = q1.popleft()
                sub_result.append(node.val)
                if node.left: q2.append(node.left)
                if node.right: q2.append(node.right)
            
            result.append(sub_result)
            
            if not q2: continue # hackish, but, well
            
            sub_result = []
            while q2:
                node = q2.popleft()
                sub_result.append(node.val)
                if node.left: q1.append(node.left)
                if node.right: q1.append(node.right)
            
            result.append(sub_result)
        
        return result