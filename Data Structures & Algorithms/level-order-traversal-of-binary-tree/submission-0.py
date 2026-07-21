# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        traverse using BFS and append node.vals into a list
        append the list after each level
        '''
        #when the tree is empty
        if not root:
            return []

        res = []

        node_queue = deque([root])

        while node_queue:
            len_queue = len(node_queue)
            temp = []

            for _ in range(len_queue):
                cur_node = node_queue.popleft()
                
                if cur_node.left:
                    node_queue.append(cur_node.left)
                
                if cur_node.right:
                    node_queue.append(cur_node.right)
                
                temp.append(cur_node.val)
            
            res.append(temp)

        return res


        '''

        root = [1,2,3,4,5,6,7]
        res = [ [1], [2, 3], [4, 5, 6, 7]]

        node_queue : 6 7

        len_queue = 4
        cur_node = 4
        temp = 

        Time Complexity: O(n) 
        Space Complexity: O(n)
        '''


        