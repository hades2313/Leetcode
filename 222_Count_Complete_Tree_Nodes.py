# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 遍历，O(number of nodes)
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def count(root):
            if not root:
                return
            result[0] += 1
            count(root.left)
            count(root.right)
        result = [0]
        count(root)
        return result[0]

# 也是暴力解
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# O(h ^ 2) where h = logn
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_depth(root):
            return 0 if not root else 1 + get_depth(root.left)
        if not root:
            return 0
        left_depth, right_depth = get_depth(root.left), get_depth(root.right)
        if left_depth == right_depth:
            return 1 + 2 ** left_depth - 1 + self.countNodes(root.right)
        return 1 + 2 ** right_depth - 1 + self.countNodes(root.left)