# okay I did this so many friken ways to try and make the logic as clean as it should be
# and I'm still not happy with it

# but
# 60ms, 82.56%, 18Mb, 88.55%

# oh, and I just noticed my solution to 199 (which also walked a tree) was solved with even more case switches
# so, I guess, I've always been bad at this? anyway that is relaxing somehow
from typing import Optional
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        reversing = False
        
        node = root # just changing the name, nothing special about root
        
        stack = [TreeNode(0)]
        
        while True:
            
            while node.left and not reversing:
                stack.append(node)
                node = node.left
            
            if not reversing:
                k -= 1
                if k == 0: return node.val
            
            if node.right:
                reversing = False
                stack.append(node)
                node = node.right
                continue
            
            reversing = True
            
            previousNode, node = node, stack.pop()
            while previousNode == node.right:
                previousNode, node = node, stack.pop()
            
            if not stack: break
            
            k -= 1
            if k == 0: return node.val
        
        return 'tree too small'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    
    def __repr__(self):
        return "TN:%i " % (self.val)

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

vals = [5,3,6,2,4,None,None,1]
vals = [38,15,97,13,17,None,None,2,None,None,None,1,5,-86,None,None,None,None,-60,-70,-15]


# seems to be working, but ugly:
# (I mean, even without the print debugging)
class SolutionLotsOfIfBranches:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        node = root # I don't think this is necessary
        
        stack = []
        nodeWeCameFrom = None
        while True:
            
            if nodeWeCameFrom not in (node.left, node.right) and node.left:
                print('going down and left at node', node)
                print('stack :', stack, '\n')
                stack.append(node)
                node, nodeWeCameFrom = node.left, node
                continue
            
            if nodeWeCameFrom not in (node.left, node.right) and node.right:
                print('going down and right at node', node)
                print('stack :', stack, '\n')
                k -= 1
                if k == 0: return node.val
                stack.append(node)
                node, nodeWeCameFrom = node.right, node
                continue
            
            if not node.left and not node.right:
                print('going back up from leaf node', node)
                print('stack :', stack, '\n')
                k -= 1
                if k == 0: return node.val
                node, nodeWeCameFrom = stack.pop(), node
                continue
            
            if nodeWeCameFrom == node.left:
                print('came from left at node', node)
                print('stack :', stack, '\n')
                k -= 1
                if k == 0: return node.val
                if node.right:
                    stack.append(node)
                    node, nodeWeCameFrom = node.right, node
                else:
                    node, nodeWeCameFrom = stack.pop(), node
                continue
            
            if nodeWeCameFrom == node.right:
                print('came from right at node', node)
                print('stack :', stack, '\n')
                node, nodeWeCameFrom = stack.pop(), node
                continue

# I didn't even test this it might totally have a bug
# but also I don't like the increment once before and then at the end of the while loop
# (because it refers to the node you're just about to pop)
# I tried a few different refactorings but they all seemed as goofy
class SolutionRecursive:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        return self.kthSmallest2(root,k)[1]
    
    def kthSmallest2(self, root, k):
        
        raise Exception("I haven't even tested this")
        
        if root == None: return k, None
        
        node = root #don't need to do this
        
        stack = [node]
        
        while node.left:
            node = node.left
            stack.append(node)
        k -= 1
        
        while stack:
            node = stack.pop()
            if k == 0: return k, node.val
            if node.right:
                k, val = self.kthSmallest2(node,k)
                if k == 0: return k, node.val
            k -= 1
        
        return k, node.val