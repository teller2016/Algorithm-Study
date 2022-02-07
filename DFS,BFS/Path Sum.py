# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, target):
            cur_val = target - node.val
            if node.left is None and node.right is None:
                if cur_val == 0:
                    return True
                else:
                    return False

            left, right = False, False
            if node.left:
                left = dfs(node.left, cur_val)
            if node.right:
                right = dfs(node.right, cur_val)

            return left or right

        if root is None:
            return False

        return dfs(root, targetSum)