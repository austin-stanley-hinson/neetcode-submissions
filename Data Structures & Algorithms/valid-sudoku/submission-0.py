class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = {i : set() for i in range(9)}
        col_map = {i : set() for i in range(9)}
        square_map = {}

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if (r//3, c//3) not in square_map:
                    square_map[(r//3, c//3)] = set()
                
                if (
                    board[r][c] in row_map[r] or 
                    board[r][c] in col_map[c] or 
                    board[r][c] in square_map[(r//3, c//3)]
                ):
                    return False 

                row_map[r].add(board[r][c])
                col_map[c].add(board[r][c])
                square_map[(r//3, c//3)].add(board[r][c])

        return True

        '''
        row_map  = { 0 : {1,2,3} , 1 :{4}, 2:{}, 3:{} , 4:{} , 5:{}, 6:{},  7:{}, 8 :{} }
        col_map = { 0 : {1,4} , 1 :{2}, 2:{}, 3:{} , 4:{3} , 5:{}, 6:{},  7:{}, 8 :{} }

        square_map = {(0,0):{1,4}, (0,1):{3}}

        r = 1, c = 0

        (0,0) (0,0) ()

        
    
        }






        '''