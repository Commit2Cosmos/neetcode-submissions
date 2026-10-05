# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], min_val=None, max_val=None) -> bool:
        if min_val is None:
            min_val = -1000000001
        if max_val is None:
            max_val = 1000000001

        res = True
        if root.left:
            if root.left.val >= root.val or root.left.val <= min_val or root.left.val >= max_val:
                res = False
                return res

            res &= self.isValidBST(root.left, min_val, root.val)

        if root.right:
            if root.right.val <= root.val or root.right.val <= min_val or root.right.val >= max_val:
                res = False
                return res

            res &= self.isValidBST(root.right, root.val, max_val)
            

        return res