"""
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node
down to the farthest leaf node

"""
__author__ = "Shruthi"


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maximum_depth_of_a_tree(self, root):
        """
        :param root: TreeNode
        :return: int
        """
        if root is None:
            return 0
        left_depth = self.maximum_depth_of_a_tree(root.left)
        right_depth = self.maximum_depth_of_a_tree (root.right)

        return max(left_depth, right_depth)+1


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    sol = Solution()
    print("Maximum depth of the tree is :", sol.maximum_depth_of_a_tree(root))