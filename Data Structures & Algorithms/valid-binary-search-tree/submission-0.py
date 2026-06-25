# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low = float('-inf')
        high = float('inf')
        def dfs(node, low, high):
            if not node:
                return True
            if low < node.val < high:
                # This is a valid BST, so we contiue:
                return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
            else:
                return False
        return dfs(root, low, high)