# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    #68ms, 7.19%, memory low variance
    def invertTreeExtraDef(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def flipNode(node):
            temp = node.left
            node.left = node.right
            node.right = temp
            
            if node.left:
                flipNode(node.left)
            
            if node.right:
                flipNode(node.right)
        
        if root:
            flipNode(root)
        
        return root
    
    #78ms, 5.46%, okay surprising
    def invertTreeSelfRecurse(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root:
            temp = self.invertTree(root.left)
            root.left = self.invertTree(root.right)
            root.right = temp
        
        return root
    
    
    #51ms, 39.00%
    def invertTreeDFS_question_mark(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # note for DFS a list is fine (though it's a not detectably different runtime)
        from collections import deque
        
        queue = deque([root])
        
        while queue:
            node_in_question = queue.pop()
            if node_in_question:
                node_in_question.left, node_in_question.right = node_in_question.right, node_in_question.left
                queue.append(node_in_question.left)
                queue.append(node_in_question.right)
        
        return root
    
    #28ms, 97.42%
    # really? Why so much faster than DFS?
    def invertTreeBFS_question_mark(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque
        
        queue = deque([root])
        
        while queue:
            node_in_question = queue.popleft()
            if node_in_question:
                node_in_question.left, node_in_question.right = node_in_question.right, node_in_question.left
                queue.append(node_in_question.left)
                queue.append(node_in_question.right)
        
        return root