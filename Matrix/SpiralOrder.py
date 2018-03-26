"""
Find the clock wise Spiral Order of the given matrix

[[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]]

"""

___author__ = "Shruthi"


def calulate_spriral_order(input_matrix):
    """
    :param input_matrix: List[List[]]
    :return: List[]
    """
    top = 0
    left = 0
    bottom = len(input_matrix) - 1
    right = len(input_matrix[0]) - 1
    direction = 0
    result = []

    while top < bottom+1 and left < right+1:
        if direction == 0:
            for i in range(left, right+1):
                result.append(input_matrix[top][i])
            top = top + 1
        elif direction == 1:
            for i in range(top, bottom+1):
                result.append(input_matrix[i][right])
            right = right - 1
        elif direction == 2:
            for i in range(right, left-1, -1):
                result.append(input_matrix[bottom][i])
            bottom = bottom - 1
        elif direction == 3:
            for i in range(bottom, top-1, -1):
                result.append(input_matrix[i][left])
            left = left + 1
        direction = (direction + 1) % 4
    return result


if __name__ == "__main__":
    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print("The spiral order in clockwise direction is: ")
    print(calulate_spriral_order(A))
