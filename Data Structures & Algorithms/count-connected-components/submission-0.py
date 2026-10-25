class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        use a dfs approach
        count the num of components as the num of dfs calls I make
            -I make dfs from nodes not yet added to visited

        '''

        adj_list = {i:[] for i in range(n)}

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
        numComponents = 0

        def dfs(node):

            visited.add(node)

            for nei in adj_list[node]:
                if nei not in visited:
                    dfs(nei)
            
            return 

        for node in range(n):
            if node not in visited:
                numComponents += 1 
                dfs(node)
        
        return numComponents