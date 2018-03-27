"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node
down to the nearest leaf node

"""


class TreeNode(object):
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None


class Solution(object):
    def minimum_depth_of_a_tree(self, root):
        """
        :param root: TreeNode
        :return: int
        """

        if root is None:
            return 0

        left_depth = self.minimum_depth_of_a_tree(root.left)
        right_depth = self.minimum_depth_of_a_tree(root.right)

        return min(left_depth, right_depth) + 1


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    sol = Solution()
    print("Minimum depth of the tree is :", sol.minimum_depth_of_a_tree(root))