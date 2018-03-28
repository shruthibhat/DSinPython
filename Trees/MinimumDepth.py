"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node
down to the nearest leaf node

"""

__author__ = "Shruthi"


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

        if left_depth is 0:
            return left_depth + 1
        elif right_depth is 0:
            return right_depth + 1

        return min(self.minimum_depth_of_a_tree(root.left), self.minimum_depth_of_a_tree(root.right)) + 1


if __name__ == "__main__":
    TreeNode1 = TreeNode(3)
    TreeNode1.left = TreeNode(9)
    TreeNode1.right = TreeNode(20)
    TreeNode1.right.left = TreeNode(15)
    TreeNode1.right.right = TreeNode(7)
    sol = Solution()

    TreeNode2 = TreeNode(2)
    TreeNode2.left = TreeNode(10)
    print("Minimum depth of the TreeNode1 is :", sol.minimum_depth_of_a_tree(TreeNode1))
    print("Minimum depth of the TreeNode2 is :", sol.minimum_depth_of_a_tree(TreeNode2))
