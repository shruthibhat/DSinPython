"""
A robot is located at the top-left corner of a m X n. the robot can move either right or down at a given point.
The robot is trying to reach the bottom right corner of the grid. How many possible unique paths are there
"""
__author__ = "Shruthi"


def calculate_unique_paths(m, n):
    # Initialize a matrix of size [m+1][m+2]

    matrix = [[0 for j in range(n+1)] for i in range(m+1)]
    # The total unique paths at grid (r, c) are equal to the sum of total unique paths from grid to the
    # right (r, c + 1) and the grid below (r + 1, c).
    matrix[m-1][n] = 1

    for row in range(m-1, -1, -1):
        for col in range(n-1, -1, -1):
            matrix[row][col] = matrix[row+1][col] + matrix[row][col+1]

    return matrix[0][0]


if __name__ == '__main__':
    print ("The number of unique paths possible are :", calculate_unique_paths(3, 7))