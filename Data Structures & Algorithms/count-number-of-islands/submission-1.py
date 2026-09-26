class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0 

        def dfs(row, col):

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_row = row + dr
                new_col = col + dc 

                if (
                    0 <= new_row < len(grid) and
                    0 <= new_col < len(grid[0]) and
                    grid[new_row][new_col] == "1"
                ):
                    grid[new_row][new_col] = "0"
                    dfs(new_row, new_col)


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    numIslands += 1
                    grid[row][col] = "0"
                    dfs(row, col)

        return numIslands 

