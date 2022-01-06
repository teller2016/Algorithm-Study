# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        queue = collections.deque([root])
        result = ['#']

        while queue:
            node = queue.popleft()

            if node:
                queue.append(node.left)
                queue.append(node.right)
                result.append(str(node.val))
            else:
                result.append('#')

        return ' '.join(result)

    def deserialize(self, data):
        if data == '# #':
            return None

        nodes = data.split()

        root = TreeNode(nodes[1])
        queue = collections.deque([root])
        index = 2

        while queue:
            node = queue.popleft()
            if nodes[index] != '#':
                node.left = TreeNode(nodes[index])
                queue.append(node.left)
            index += 1

            if nodes[index] != '#':
                node.right = TreeNode(nodes[index])
                queue.append(node.right)
            index += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))