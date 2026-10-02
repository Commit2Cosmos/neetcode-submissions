# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res

        stack = [(root, 0)]

        while len(stack) > 0:
            curr, i = stack.pop()
            if i == len(res):
                res.append(curr.val)
            else:
                res[i] = curr.val


            if curr.right:
                stack.append((curr.right, i+1))
            if curr.left:
                stack.append((curr.left, i+1))

        return res
            
