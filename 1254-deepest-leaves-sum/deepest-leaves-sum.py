# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def maxdepth(node):
            if not node:
                return 0
            elif node.right and not node.left:
                return 1 + maxdepth(node.right)
            elif node.left and not node.right:
                return 1+maxdepth(node.left)
            else:
                return 1 + max(maxdepth(node.right),maxdepth(node.left))
        
        height = maxdepth(root)
        count = 0
        res = []
        def checker(root,count):
            if not root:
                return
            elif root.right and not root.left:
                if count == height:
                    res.append(root.val)
                elif count<height:
                    count+=1
                    checker(root.right,count)
            elif root.left and not root.right:
                if count == height:
                    res.append(root.val)
                elif count<height:
                    count+=1
                    checker(root.left,count)
            else:
                if count == height:
                    res.append(root.val)
                checker(root.right,count+1)
                checker(root.left,count+1)
            return res
        return sum(checker(root,1))