# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        nodeList = []

        if not root:
            return ""

        q = deque([root])

        while q:
            node = q.popleft()

            if node:
                nodeList.append(str(node.val))
            else:
                nodeList.append("N")
                continue

            if node.left:
                q.append(node.left)
            else:
                q.append(None)

            if node.right:
                q.append(node.right)
            else:
                q.append(None)

        return "#".join(nodeList)

        '''
        nodeList = ["1", "2", "3", "N", "N", "4", "5" , "N", "N", "N", "N"]
        
        "1#2#3#N#N#4#5#N#N#N#N"

        '''

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        '''
        returned serialiazed tree is based of BFS traversal
        [1,2,3,N,N,4,5,N,N,N,N]
         root = Tree(1)
         queue = 5

         DRY RUN:
         nodeList = [1,2,3,N,N,4,5,N,N,N,N]

         root = TreeNode(1)
                    left = 2
                        left = None 
                        right = None
                    right = 3
                        left = 4
                            left = None
                            right = None
                        right = 5

         index = 8

         q = 5

         curr = 4

        
        '''
        if not data:
            return None 

        nodeList = data.split("#") #[1,2,3,N,N,4,5,N,N,N,N]

        root = TreeNode(int(nodeList[0]))

        q = deque([root])
        index = 1 

        while q:
            cur_node = q.popleft()

            if index < len(nodeList) and nodeList[index] != "N": #1, 3, 5
                cur_node.left = TreeNode(int(nodeList[index]))
                q.append(cur_node.left)
            
            index += 1

            if index < len(nodeList) and nodeList[index] != "N": #2, 4, 6
                cur_node.right = TreeNode(int(nodeList[index]))
                q.append(cur_node.right)
            
            index += 1 #3, 5, 7

        return root 
















