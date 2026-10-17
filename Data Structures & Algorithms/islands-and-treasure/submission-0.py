class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        shortest BFS algorithm 
        visit the neighbors that are not -1
        if a neighbor is 0 we have reached a treasure chest so can modify that pos

        (r, c, step)
        multi-source BFS problem 
        '''

        queue = deque()
        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row, col, 0))
                    visited.add((row, col))
        
        while queue: 
            cur_row, cur_col, cur_step = queue.popleft()

            grid[cur_row][cur_col] = cur_step

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_row = cur_row + dr 
                new_col = cur_col + dc 

                if (
                    0 <= new_row < len(grid) and 
                    0 <= new_col < len(grid[0]) and 
                    grid[new_row][new_col] == 2147483647 and 
                    (new_row, new_col) not in visited
                ):
                    queue.append((new_row, new_col, cur_step + 1))
                    visited.add((new_row, new_col))


   


            

        
        

