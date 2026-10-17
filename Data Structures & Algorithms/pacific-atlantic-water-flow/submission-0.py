class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        start from the oceans into the cells

        cells with row == 0, and col == 0 will flow into pacific 
        cells with row == maxRow and col == maxCol will flow into Atlantic

        keeping two sets and finding intersection after 
        use BFS to find qualifying neighbors such that heights >= 
        '''
        maxRow = len(heights)
        maxCol = len(heights[0])

        intoPacific = set()
        intoAtlantic = set()

        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if (row == 0 or col == 0):
                    intoPacific.add((row, col))

                if (row == maxRow - 1 or col == maxCol - 1):
                    intoAtlantic.add((row, col))
        
        queue = deque([pos for pos in intoPacific])
        
        while queue:
            cur_row, cur_col = queue.popleft()

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_row = cur_row + dr
                new_col = cur_col + dc 

                if (
                    0 <= new_row < maxRow and 
                    0 <= new_col < maxCol and 
                    heights[new_row][new_col] >= heights[cur_row][cur_col] and
                    (new_row, new_col) not in intoPacific
                ):
                    intoPacific.add((new_row, new_col))
                    queue.append((new_row, new_col))

        queue = deque([pos for pos in intoAtlantic])
        
        while queue:
            cur_row, cur_col = queue.popleft()

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_row = cur_row + dr
                new_col = cur_col + dc 

                if (
                    0 <= new_row < maxRow and 
                    0 <= new_col < maxCol and 
                    heights[new_row][new_col] >= heights[cur_row][cur_col] and
                    (new_row, new_col) not in intoAtlantic
                ):
                    intoAtlantic.add((new_row, new_col))
                    queue.append((new_row, new_col))

        
        return [pos for pos in intoAtlantic if pos in intoPacific]

        







