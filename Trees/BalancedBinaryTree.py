
"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as a binary tree in which the
depth of the two subtrees of every node never differs by more than 1.

"""

__author__ = "Shruthi"


class TreeNode(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


class Solution(object):
    def balanced_binary_tree(self, root):
        """
        :param root: TreeNode
        :return: boolean
        """

        return self.max_depth(root) is not -1

    def max_depth(self, root):
        """

        :param root: TreeNode
        :return: int
        """

        if root is None:
            return 0

        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)

        if left_depth == -1:
            return -1

        if right_depth == -1:
            return -1

        if abs(left_depth - right_depth) <= 1:
            return max(left_depth, right_depth) + 1

        return -1


if __name__ == "__main__":
    TreeNode1 = TreeNode(3)
    TreeNode1.left = TreeNode(9)
    TreeNode1.right = TreeNode(20)
    TreeNode1.right.left = TreeNode(15)
    TreeNode1.right.right = TreeNode(7)
    sol = Solution()

    TreeNode2 = TreeNode(234)

    TreeNode3 = TreeNode(100)
    TreeNode3.right = TreeNode(200)
    TreeNode3.right.right = TreeNode(300)

    print ("Whether tree TreeNode1 balaned?: ", sol.balanced_binary_tree(TreeNode1))
    print ("Whether tree TreeNode2 balaned?: ", sol.balanced_binary_tree(TreeNode2))
    print ("Whether tree TreeNode3 balaned?: ", sol.balanced_binary_tree(TreeNode3))


