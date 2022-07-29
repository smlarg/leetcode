# Rank 1,029,876
# 16 medium, 52.3%

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


adjList = [[2,4],[1,3],[2,4],[1,3]]

nodes = []
for i in range(len(adjList)):
    nodes.append(Node(i+1))

for i,x in enumerate(adjList):
    for y in x:
        nodes[i].neighbors.append(nodes[y-1])

# 96ms, 5.51%, but like, it's right
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node: return None
        
        new_node = Node(node.val)
        
        to_link = [new_node]
        
        bothways = {}
        bothways[new_node] = node
        bothways[node] = new_node
        while to_link:
            node_needs_linking = to_link.pop()
            old_node = bothways[node_needs_linking]
            for neighbor_node in old_node.neighbors:
                if neighbor_node in bothways:
                    node_needs_linking.neighbors.append(bothways[neighbor_node])
                else:
                    newer_node = Node(neighbor_node.val)
                    to_link.append(newer_node)
                    node_needs_linking.neighbors.append(newer_node)
                    bothways[neighbor_node] = newer_node
                    bothways[newer_node] = neighbor_node
        
        return new_node     
                    


# 48ms, 72.80%, so like, whatever
class Solution:
    def cloneGraphCheating(self, node: 'Node') -> 'Node':
        from copy import deepcopy
        return deepcopy(node)