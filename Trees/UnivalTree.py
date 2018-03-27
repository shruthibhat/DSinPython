"""
Check if given tree has equal values at all nodes

"""


class TreeNode(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


class Solution(object):
    def unival_tree(self, root):
        """
        :param root: TreeNode
        :return: int
        """

        if root is None:
            return True

        left_value = self.unival_tree(root.left)
        right_value = self.unival_tree(root.right)

        if left_value is False and right_value is False:
            return False

        if root.left and root.value != root.left.value:
            return False

        if root.right and root.value != root.right.value:
            return False

        return True


if __name__ == "__main__":
    TreeNode1 = TreeNode(1)
    TreeNode1.left = TreeNode(1)
    TreeNode1.right = TreeNode(1)
    TreeNode1.right.left = TreeNode(1)
    TreeNode1.right.right = TreeNode(1)
    sol = Solution()

    TreeNode2 = TreeNode(2)
    TreeNode2.left = TreeNode(2)

    TreeNode3 = TreeNode(12)
    TreeNode3.right = TreeNode(2)

    print("Is TreeNode1 unival? :", sol.unival_tree(TreeNode1))
    print("Is TreeNode2 unival? :", sol.unival_tree(TreeNode2))
    print("Is TreeNode3 unival? :", sol.unival_tree(TreeNode3))

