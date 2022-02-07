# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, result):
        if not root:
            return
        result.append(root.val)

        self.dfs(root.left, result)
        self.dfs(root.right, result)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result = []
        self.dfs(root1, result)
        self.dfs(root2, result)

        return sorted(result)