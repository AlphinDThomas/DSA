# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def inorder(node,res):

            if node is None:
                return 
            inorder(node.left,res)
            res.append(node.val)
            inorder(node.right,res)
            return res

        res = inorder(root, [])
        prev = res[0]
        for i in range(1,len(res)):
            if res[i]>prev:
                prev= res[i]
            else:
                return False
        return True