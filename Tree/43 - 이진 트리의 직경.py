# https://leetcode.com/problems/diameter-of-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            left = right = 0
            if node.left:
                left = dfs(node.left) + 1
            if node.right:
                right = dfs(node.right) + 1

            self.longest = max(self.longest, left +right)

            return max(left, right)

        dfs(root)

        return self.longest