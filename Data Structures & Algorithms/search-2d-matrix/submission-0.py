class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        matrix = [[1,2,4,8],
                            l
                       m
                         r 
                    l = 2, r = 3

                  [10,11,12,13],
                    l.
                    m       
                    r
                    l= 0, r = 0
                  [14,20,30,40]], target = 10
        '''

        
        for row in matrix:

            l, r = 0, len(matrix[0]) - 1

            while l <= r:
                mid = (l + r)//2 

                if row[mid] == target:
                    return True

                elif row[mid] < target:
                    l = mid + 1 
                else:
                    r = mid - 1 
        
        return False 

        '''
        target = 10 
        l = 3
        r = 3
        mid = 3

            [10,11,12,13]
                         l 
                       m
                       r


        '''
            

