"""

Find the contigous subarray within an array(conataining atleast one number) that has the largest sum
For example, given the array [2, 1, -3, 4, -1, 2, 1, -5, 4]
The contigous array [4, -1, 2, 1] has the largest sum = 6

"""

__author__ = "Shruthi"


def max_sum_contigous_subarray(A):
    """
    :param A: list[]
    :return: int
    """
    max_ending_here = A[0]
    max_so_far= A[0]

    for i in range(1, len(A)):
        # The maximum value until this index
        max_ending_here = max(max_ending_here + A[i], A[i])
        # The maximum until now
        max_so_far = max(max_ending_here, max_so_far)

    return max_so_far


if __name__ == "__main__":
    A = [2, 1, -3, 4, -1, 2, 1, -5, 4]
    print ("The max sum contigous subarray for [2, 1, -3, 4, -1, 2, 1, -5, 4] is : ", max_sum_contigous_subarray(A))