"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        '''
        node.neighbors
            nodes

        hashmap { oldNodes : newNodes }

        if curNode not in the hashmap:
            curNode's neigbors 


        '''

        if not node:
            return None 

        hashMap = {}

        def dfs(n):
            if n in hashMap:
                return hashMap[n]
            
            hashMap[n] = Node(n.val)
            neighs = []
            
            for nei in n.neighbors:
                neighs.append(dfs(nei))
            
            hashMap[n].neighbors = neighs
            
            return hashMap[n]

        dfs(node)

        return hashMap[node]

        '''
        
                



        '''






