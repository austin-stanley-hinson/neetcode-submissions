class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        find all the Os at the edge of the board - store in a set (edgeset)
        traverse from the Xs at the edge towards the middle of the board 
            - we will then change any Os that pass these conditions
                -pos must be valid 
                - pos must not be in the edgeset    
            
            ["X","X","X","X"],
            ["X","O","O","O"],
            ["X","X","O","0"],
            ["0","O","0","X"]

        '''

        edgeSet = set()
        queue = deque()

        for row in range(len(board)):
            for col in range(len(board[0])):
                if (
                    row == 0 or 
                    col == 0 or 
                    row == len(board) - 1 or
                    col == len(board[0]) - 1
                ):
                    if board[row][col] == "O":
                        edgeSet.add((row, col))
                        queue.append((row, col))
        
        while queue:
            cur_row, cur_col = queue.popleft()

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_row = cur_row + dr 
                new_col = cur_col + dc 

                if (
                    0 <= new_row < len(board) and 
                    0 <= new_col < len(board[0]) and 
                    board[new_row][new_col] == "O" and 
                    (new_row, new_col) not in edgeSet
                ):
                    edgeSet.add((new_row, new_col))
                    queue.append((new_row, new_col))

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O" and (row, col) not in edgeSet:
                    board[row][col] = "X"

