# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        res1 = []
        res2 = []

        def checker1(node,res):

            if node is None:
                return 
            if not node.left and not node.right:
                res.append(node.val)
                
            if node.right and not node.left:
                checker1(node.right,res)
            if node.left and not node.right:
                checker1(node.left,res)
            if node.right and node.left:
                checker1(node.left,res)
                checker1(node.right,res)
            
            return res
        res1 = checker1(root1,[])
        res2 = checker1(root2,[])
        print(res1)
        print(res2)
        if res1 ==  res2:
            return True
        return False
       