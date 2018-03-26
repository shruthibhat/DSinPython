"""
Find the sub contiguous subarray within an array of integers that has the largest product. For example,
given the array [2, 3, -2, 4], the contiguous subarray [2,3] has the largest product = 6

"""

__author__ = "Shruthi"


def calculate_max_product_subcontiguous_array(A):
    """
    :param A: list[]
    :return: int
    """
    if len(A) > 1:
        maximum = A[0]
        minimum = A[0]
        max_answer = A[0]

        for i in range(1, len(A)):
            mx = maximum
            mn = minimum
            maximum = max(max(A[i], mx * A[i]), mn * A[i])
            minimum = min(min(A[i], mx * A[i]), mn * A[i])
            max_answer = max(maximum, max_answer)
    return max_answer


if __name__ == "__main__":
    A =[2, 3, -2, 4]
    print("The max product contigous subarray is :", calculate_max_product_subcontiguous_array(A))