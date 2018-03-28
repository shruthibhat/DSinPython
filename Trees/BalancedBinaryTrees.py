"""
Given an array where elements are sorted in ascending order, convert it to a height
balanced BST.

"""

__author__ = "Shruthi"


class TreeNode(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


class Solution(object):
    def sorted_array_to_bst(self, input_list):
        self.__build_bst(input_list, 0, len(input_list)-1)

    def __build_bst(self, input_list, start, end):
        if start > end:
            return None
        mid = (start + end) / 2

        root = TreeNode(input_list[mid])
        root.left = self.__build_bst(input_list, start, mid-1)
        root.right = self.__build_bst(input_list, mid+1, end)

        return root


if __name__ == "__main__":
    A = [2, 4, 6, 8, 10, 12, 16]
    sol = Solution()
    sol.sorted_array_to_bst(A)