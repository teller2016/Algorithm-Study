# https://leetcode.com/problems/invert-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None

        def recursive(node):
            node.left, node.right = node.right, node.left

            if node.left:
                recursive(node.left)
            if node.right:
                recursive(node.right)


        recursive(root)

        return root


# BFS, DFS 풀이
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            # node = queue.pop()    #stack으로 DFS 풀이
            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)

        return root

# DFS 풀이
