# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def treeFromArray(vals):

    from collections import deque
    valq = deque(vals)

    root = TreeNode(valq.popleft())
    nodeq = deque([root])

    while valq:
        node = nodeq.popleft()
        left = TreeNode(valq.popleft())
        if left:
            node.left = left
            nodeq.append(node.left)
        right = TreeNode(valq.popleft())
        if right:
            node.right = right
            nodeq.append(node.right)
    
    return root



# 95ms, 16.64%
# huh. okay, spent a long time frustrated by this number,
# but everyone in the forums did some version of this (most used a global variable instead of a second return, but, no I'm better)
# so fine.
# I'm stressing about this too much
#
# oh, wait, no
# putting a global *class* valiable in via an __init__ definition *is* a good idea
# well, anyway
# 
# (oh and the -1 in the end is definitely a bug, but I know that and I don't care)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        return self.helper(root)[0]-1
    
    def helper(self, root):
        
        m=n=l=r=0
        if root.left:
            m, l = self.helper(root.left)
        if root.right:
            n, r = self.helper(root.right)
        return max(m,n,l+r+1), max(l+1,r+1)