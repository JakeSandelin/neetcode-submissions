# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(n,m):
            if not n and not m:
                return True
            
            if not n or not m:
                return False

            if n.val != m.val:
                return False

            l, r = dfs(n.left,m.left), dfs(n.right,m.right)

            if l and r:
                return True
            else:
                return False

        return dfs(p,q)