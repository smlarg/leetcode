preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]


# welp. most people didn't solve it with recursion, apparently, but speed is okay
# 247ms, 45.72%, there is a solution at around 100 though,
# 89.6Mb, 5.38%, actually there are three peaks, at 20Mb, 55Mb, and 89Mb, so interesting

# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.indexDict = {}
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if len(preorder) == 0: return None
        
        for i, n in enumerate(inorder):
            self.indexDict[n] = i
        
        return self.buildTree2(preorder,inorder,0)
    
    def buildTree2(self, preorder, inorder, offset):
        
        if len(preorder) ==0: return None
        
        root = TreeNode(preorder[0])
        
        rootIndex = self.indexDict[preorder[0]] - offset
        
        lowerPreOrder = preorder[1:rootIndex+1]
        upperPreOrder = preorder[rootIndex+1:]
        lowerInOrder = inorder[:rootIndex]
        upperInOrder = inorder[rootIndex+1:]
        
        root.left = self.buildTree2(lowerPreOrder,lowerInOrder,offset)
        root.right = self.buildTree2(upperPreOrder,upperInOrder,offset + rootIndex + 1)
        
        return root

# right, why am I copying the arrays
# 152ms, 69.18%, memory still the same though because that's the recursion
class Solution:
    def __init__(self):
        self.indexDict = {}
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if len(preorder) == 0: return None
        
        for i, n in enumerate(inorder):
            self.indexDict[n] = i
        
        return self.buildTree2(preorder,inorder,0)
    
    def buildTree2(self, preorder, inorder, offset):
        
        if len(preorder) ==0: return None
        
        root = TreeNode(preorder[0])
        
        rootIndex = self.indexDict[preorder[0]] - offset
        
        root.left = self.buildTree2(preorder[1:rootIndex+1],inorder[:rootIndex],offset)
        root.right = self.buildTree2(preorder[rootIndex+1:],inorder[rootIndex+1:],offset + rootIndex + 1)
        
        return root
