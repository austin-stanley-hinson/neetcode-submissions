class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        helper function to detect cycles
        keep a visited set to see if all components are connected
        '''

        adj_list = defaultdict(list)

        for node, nei in edges:
            adj_list[node].append(nei)
            adj_list[nei].append(node)
        
        visited = set()

        def isCyclic(node, parent):
            if node in visited:
                return True
            
            visited.add(node)

            for nei in adj_list[node]:
                if nei == parent:
                    continue

                if isCyclic(nei, node):
                    return True

            return False
            
        return not isCyclic(0, -1) and len(visited) == n

