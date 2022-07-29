#c.f. Problem 236

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

vals = "[1,2]"


# well that was an unhelpful error message
# anyway, I guess I really could have read more carefully
# in the end
# 252ms, 70.21%, fine
# memory is 25% higher than almost everyone though, which is a bit odd.
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        from collections import deque
        
        if root == None: return "[]"
        
        result = []
        nodeq = deque([root])
        
        if root:
            result.append(root.val)

        while nodeq:
            node = nodeq.popleft()
            if node.left:
                result.append(node.left.val)
                nodeq.append(node.left)
            else:
                result.append(None)
            if node.right:
                result.append(node.right.val)
                nodeq.append(node.right)
            else:
                result.append(None)
        
        while result[-1] == None: result.pop()
        
        # they insist on a string!!!!! ghhahaaa!
        return str(result)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # thank you thank you thank you python for eval()!
        data = eval(data)
        from collections import deque
        if data == []:
            return None
        
        valq = deque(data)

        root = TreeNode(valq.popleft())
        nodeq = deque([root])

        while valq:
            node = nodeq.popleft()
            left = valq.popleft()
            if left != None:
                node.left = TreeNode(left)
                nodeq.append(node.left)
            # this seems a bit hackish, but, maybe not?
            if valq:
                right = valq.popleft()
                if right != None:
                    node.right = TreeNode(right)
                    nodeq.append(node.right)

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))