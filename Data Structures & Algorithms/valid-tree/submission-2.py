class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        I want to use a dfs approach 
            - keep a visited set and add to it as I visit
        There should no cycles 
            - a cycle is detected when a node is already in visited
            - I will skip over parent connections since the graph is undirected
        In the end, len(visited) == n else means some nodes were not reached in the dfs
            - Implies there were disconnected components

        '''
        #EdgeCase: if there are no nodes
        if n == 0:
            return True 

        visited = set()

        adj_list = defaultdict(list)

        for node, neigh in edges:
            adj_list[node].append(neigh)
            adj_list[neigh].append(node)

        def detectCycle(node, parent):
            if node in visited:
                return True 

            visited.add(node)

            for neigh in adj_list[node]:
                if neigh == parent:
                    continue
                
                if detectCycle(neigh, node):
                    return True 

            return False 

        return not detectCycle(0, -1) and len(visited) == n

















