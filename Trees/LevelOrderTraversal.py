"""

Breadth first Traversal or level order traversal of a binary tree


"""

__author__ = "Shruthi"

from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


class Solution(object):
    def level_order_traversal(self, root):
        """
        :param root: TreeNode
        :return: None
        """

        if root is None:
            return

        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            node = queue.pop()
            print node.value
            if node.left is not None:
                queue.appendleft(node.left)
            if node.right is not None:
                queue.appendleft(node.right)

if __name__ == "__main__":
    TreeNode1 = TreeNode(3)
    TreeNode1.left = TreeNode(9)
    TreeNode1.right = TreeNode(20)
    TreeNode1.right.left = TreeNode(15)
    TreeNode1.right.right = TreeNode(7)
    sol = Solution()

    print("Level order traversal result :", sol.level_order_traversal(TreeNode1))


