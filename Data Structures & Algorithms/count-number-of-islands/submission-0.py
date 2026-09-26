class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        numIslands = 0 
        stack = []

        def dfs():

            while stack:
                row, col = stack.pop()

                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_row = row + dr
                    new_col = col + dc 

                    if (
                        new_row >= 0 and 
                        new_row < len(grid) and
                        new_col >= 0 and 
                        new_col < len(grid[0]) and 
                        grid[new_row][new_col] == "1" and 
                        (new_row, new_col) not in visited
                    ):
                        visited.add((new_row, new_col))
                        stack.append((new_row, new_col))


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    numIslands += 1
                    stack.append((row, col))
                    dfs()

        return numIslands 

