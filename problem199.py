# 33 medium, 67.0%

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
        if left != None:
            node.left = TreeNode(left)
            nodeq.append(node.left)
        if valq:
            right = valq.popleft()
            if right != None:
                node.right = TreeNode(right)
                nodeq.append(node.right)
    
    return root


vals = [1,2,3,None,5,None,4]

t = treeFromArray(vals)

# slow rank, but only about 30% slower than the median, so it would just need tweeking
# 65ms, 16.47%

# it is 2n running time (you visit a node once for itself, then once more for each child it has
# (so runtime = nodes + edges)
# but there's no way to beat O(n) for sure, and I think 2n is about the best
# 
# the code does lack grace - so many cases! - but you can be going up or down, left or right,
# and they're all different, so I think that's kind of what it is
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        result = []
        stack = [None]
        node = root
        level = 1
        previous = -1

        while stack:
        #for _ in [1]:
            if node == None:
                print("break")
                break
            if previous == node.right:
                if node.left:
                    previous = node
                    node = node.left
                    stack.append(previous)
                    level += 1
                    continue
                else:
                    previous = node
                    node = stack.pop()
                    level -=1
                    continue
            if previous == node.left:
                previous = node
                node = stack.pop()
                level -= 1
                continue
            if level > len(result):
                result.append(node.val)
            if node.right:
                previous = node
                stack.append(previous)
                node = node.right
                level +=1
                continue
            if node.left:
                previous = node
                stack.append(previous)
                node = node.left
                level +=1
                continue
            else:
                previous = node
                node = stack.pop()
                level -=1
        
        return result
                
        
        