# rank unchanged
# medium 25, 61.6%

# c.f. https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# but now the tree is unsorted? okay.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

vals = [3,5,1,6,2,0,8,None,None,7,4]
p, q = 5, 1
p, q = 5, 4

def treeFromArray(vals):

    from collections import deque
    valq = deque(vals)

    root = TreeNode(valq.popleft())
    nodeq = deque([root])

    while valq:
        node = nodeq.popleft()
        left = valq.popleft()
        if left != None:
            node.left = TreeNode(left)
            nodeq.append(node.left)
        if valq:
            right = valq.popleft()
            if right != None:
                node.right = TreeNode(right)
                nodeq.append(node.right)
    
    return root

# 1579ms, 5.01%, about 15 times the median,
# so definetly wrong.
# ... but how? The tree is unsorted...
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # tree isn't sorted, nothing to do but two depth-first searches
        # no, I was extremely wrong about that. hmm.
        p_path = self.pathToGuy(root,p)
        q_path = self.pathToGuy(root,q)
        
        result = p_path[-1]
        while p_path and q_path:
            p_guy = p_path.pop()
            q_guy = q_path.pop()
            if p_guy == q_guy: result = p_guy
            else: break
        
        return result
        
    
    def pathToGuy(self,root,p):
        if root == p:
            return [root]
        if root.left:
            left_path = self.pathToGuy(root.left,p)
            if left_path :
                return left_path + [root]
        if root.right:
            right_path = self.pathToGuy(root.right,p)
            if right_path:
                return right_path + [root]
        
        return False


# from the forums. I admit it's more clever, but it's still an O(n) search no?
# well it's much much faster, but I don't understand why
# I guess it's the pre-factor of only having to find p *or* q
# which I guess is about 4 (min of two random numbers between 0 and 1, rather than sum; that's, what is that, there's an exact solution)
# so okay, prefactors matter, fine, I suppose
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root == p or root == q: return root
        
        left = right = None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p,q)
        
        if root.right:
            right = self.lowestCommonAncestor(root.right,p,q)
        
        if left and right: # this will only happen once, at LCA
            return root
        
        return left or right