class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0
        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == 1:
                    queue = deque([(row, col)])
                    visited.add((row, col))
                    area = 0

                    while queue:
                        curRow, curCol = queue.popleft()
                        area += 1
                        maxArea = max(area, maxArea)

                        for dr, dc in [(1, 0), (0,1), (-1, 0), (0, -1)]:
                            newRow = curRow + dr
                            newCol = curCol + dc 

                            if (
                                0 <= newRow < len(grid) and 
                                0 <= newCol < len(grid[0]) and 
                                (newRow, newCol) not in visited and
                                grid[newRow][newCol] == 1
                            ):
                                visited.add((newRow, newCol))
                                queue.append((newRow, newCol))

                    maxArea = max(area, maxArea)
        return maxArea 


