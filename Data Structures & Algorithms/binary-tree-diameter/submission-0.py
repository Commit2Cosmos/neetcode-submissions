# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        answ = [0]
        
        def recur(curr):
            deepest_left = 0
            if curr.left:
                deepest_left = 1 + max(deepest_left, recur(curr.left))

            deepest_right = 0
            if curr.right:
                deepest_right = 1 + max(deepest_right, recur(curr.right))

            answ[0] = max(answ[0], deepest_left + deepest_right)
            
            return max(deepest_left, deepest_right)

        return max(recur(root), answ[0])
