"""

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

"""


__author__ = "Shruthi"


def uniquePathsWithObstacles(obstaclegrid):
    """
    :type obstaclegrid: List[List[int]]
    :rtype: int
    """
    m = len(obstaclegrid)
    n = len(obstaclegrid[0])

    matrix = [[0 for j in range(n + 1)] for i in range(m + 1)]

    matrix[m - 1][n] = 1
    for row in range(m-1, -1, -1):
        for col in range(n-1, -1, -1):
            if obstaclegrid[row][col] is 1:
                matrix[row][col] = 0
            else:
                matrix[row][col] = matrix[row][col + 1] + matrix[row + 1][col]

    return matrix[0][0]


if __name__ == '__main__':
    query = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print "The number of unique paths possible are :", uniquePathsWithObstacles(query)