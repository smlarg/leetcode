# so this was a terrible approach, that I just kept banging on
# I'm going to try to resist doing it, but now I'm pretty sure this logic can be captured much quicker with a list
# something like

'''
from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1: return [0]
        if n == 2: return edges[0]
        
        linkArray = [[] for _ in range(n)]
        
        for edge in edges:
            linkArray[edge[0]].append(edge[1])
            linkArray[edge[1]].append(edge[0])
        
        node = 0
        nodeStack = [node]
        linksStack = [linkArray[node]]
        
        ...
'''
# I don't know, something like that
# anyway, that was a miserable morning.


edgeses = [\
[[3,0],[3,1],[3,2],[3,4],[5,4]],\
[[1,0],[1,2],[1,3]],\
[ [0,1], [1,2], [1,3], [3,5], [5,4] ,[5,6], [3,7], [7,8] ,[7,9] ,[9,10], [10,11]],\
[ [0,1], [1,2], [1,3], [3,5], [5,4] ,[5,6], [3,7], [7,8] ,[7,9] ,[9,10], [10,11], [11,12]]\
]

# slow and huge but at least it's something
# 1309ms, 11.01%, correct is around 750,
# 45.8Mb, correct is around 25, and I am off the flipping chart

class nodeMan:
    def __init__(self,val):
        self.val = val
        self.neighbors = []
        self.maxToLeaf = 0
        self.maxNeighbor = None
        self.secondMax = 0
    
    def __repr__(self):
        return "Node with val: %i" %  (self.val)
    
    def goAllWays(self):
        
        for neighbor in self.neighbors:
            distanceGoingThisWay = neighbor.goOutOnly(self)
            if distanceGoingThisWay >= self.maxToLeaf:
                self.secondMax = self.maxToLeaf
                self.maxToLeaf = distanceGoingThisWay
                self.maxNeighbor = neighbor
            elif distanceGoingThisWay > self.secondMax:
                self.secondMax = distanceGoingThisWay
            
        if self.secondMax == self.maxToLeaf:
            return [self.val]
            
        if self.secondMax == self.maxToLeaf - 1:
            return [self.val, self.maxNeighbor.val]
        
        return self.maxNeighbor.reportLastEdge(self)
        

    def goOutOnly(self, other):
        if len(self.neighbors) == 1:
            return 1
        
        for neighbor in self.neighbors:
            if neighbor is other: continue
            distanceGoingThisWay = neighbor.goOutOnly(self)
            if distanceGoingThisWay >= self.maxToLeaf:
                self.secondMax = self.maxToLeaf
                self.maxToLeaf = distanceGoingThisWay
                self.maxNeighbor = neighbor
            elif distanceGoingThisWay > self.secondMax:
                self.secondMax = distanceGoingThisWay
        
        return self.maxToLeaf + 1
        
    
    def reportLastEdge(self, other):
        if other.secondMax +1 >= self.maxToLeaf:
            self.secondMax = self.maxToLeaf
            self.maxToLeaf = other.secondMax + 1
            # self.maxNeighbor can be skipped
            # because at this point you've hit the money
            # I think
        elif other.secondMax +1 > self.secondMax:
            self.secondMax = other.secondMax + 1
        
        if self.secondMax == self.maxToLeaf:
                return [self.val]
            
        if self.secondMax == self.maxToLeaf - 1:
            return [self.val, self.maxNeighbor.val]
        
        return self.maxNeighbor.reportLastEdge(self)
        
from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1: return [0]
        if n == 2: return edges[0]
        
        nodes = {}
        
        nodeVal1, nodeVal2 = edges[0][0], edges[0][1]
        
        node1 = nodes[nodeVal1] = nodeMan(nodeVal1)
        node2 = nodes[nodeVal2] = nodeMan(nodeVal2)
        
        node1.neighbors.append(node2)
        node2.neighbors.append(node1)
        
        fakeRoot = node1
        
        for pair in edges[1:]:
            val1, val2 = pair[0],pair[1]
            if val1 in nodes:
                node1 = nodes[val1]
            else:
                node1 = nodes[val1] = nodeMan(val1)
            if val2 in nodes:
                node2 = nodes[val2]
            else:
                node2 = nodes[val2] = nodeMan(val2)
            node1.neighbors.append(node2)
            node2.neighbors.append(node1)
        
        return fakeRoot.goAllWays()
        