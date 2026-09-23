# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is not None and q is not None:
            pass
        elif p is None and q is None:
            return True
        else:
            return False

        stack = [(p, q)]

        while len(stack) > 0:
            curr_p, curr_q = stack.pop()
            if curr_p.val != curr_q.val:
                return False
            if curr_p.right is not None and curr_q.right is not None:
                stack.append((curr_p.right, curr_q.right))
            elif curr_p.right is None and curr_q.right is None:
                pass
            else:
                return False

            if curr_p.left is not None and curr_q.left is not None:
                stack.append((curr_p.left, curr_q.left))
            elif curr_p.left is None and curr_q.left is None:
                pass
            else:
                return False

        return True