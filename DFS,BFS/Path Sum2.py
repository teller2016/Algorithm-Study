# https://leetcode.com/problems/path-sum-ii/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(cur, target, route):
            if cur:
                target -= cur.val
                new_route = route + [cur.val]

                if target == 0 and cur.left is None and cur.right is None:
                    result.append(new_route)
                    return

                dfs(cur.left, target, new_route)
                dfs(cur.right, target, new_route)

        if not root:
            return []

        dfs(root, targetSum, [])

        return result