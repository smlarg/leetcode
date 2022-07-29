vals, p, q = [6,2,8,0,4,7,9,null,null,3,5], 2, 8

vals, p, q = [6,2,8,0,4,7,9,null,null,3,5], 2, 4

vals, p, q = [2,1], 2, 1

vals, p, q = [2,null,3], 3, 2

vals, p, q = [2,1], 1, 2

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

vals = [6,2,8,0,4,7,9,None,None,3,5]

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
        right = valq.popleft()
        if right != None:
            node.right = TreeNode(right)
            nodeq.append(node.right)
    
    return root


class Solution:
    # 144ms, 24.28%, little variance in memory
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        from collections import deque
        
        chain_p = deque([root])
        node = root
        while node.val != p.val:
            if p.val < node.val:
                node = node.left
            else:
                node = node.right
            chain_p.append(node)
        
        chain_q = deque([root])
        node = root
        while node.val != q.val:
            if q.val < node.val:
                node = node.left
            else:
                node = node.right
            chain_q.append(node)
        
        result = root
        while chain_p and chain_q:
            r = chain_p.popleft()
            s = chain_q.popleft()
            if r.val == s.val:
                result = r
        
        return result


    # 178ms - what?!?
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        from collections import deque
        
        chain_p = deque()
        node = root
        while node.val != p.val:
            if p.val < node.val:
                node = node.left
            else:
                node = node.right
            chain_p.append(node)
        
        result = root
        
        node = root
        while (node.val != q.val) and chain_p:
            if q.val < node.val:
                node = node.left
            else:
                node = node.right
            p_node = chain_p.popleft()
            if p_node is node:
                result = node
            else:
                break
        
        return result
    
    # 138ms, 30.01%, huh. still overthinking?
    def lowestCommonAncestor3(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # okay, right, I was overthinking this. (I keep doing that.)
        p = p.val
        q = q.val
        
        result = root
        while True:
            r = result.val
            if (p<=r) != (q<=r): return result
            if (p==r) or (q==r): return result
            if (p<r): result = result.left
            else: result = result.right
    
    # 112ms, 57.23%; more better than I expected, but, I still don't know what the right answer is
    def lowestCommonAncestor4(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        while True:
            if (p.val<=root.val) != (q.val<=root.val): return root
            if (p.val==root.val) or (q.val==root.val): return root
            if (p.val<root.val): root = root.left
            else: root = root.right