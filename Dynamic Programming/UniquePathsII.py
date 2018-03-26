"""

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

"""


def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    matrix = [[0 for j in range(n + 1)] for i in range(m + 1)]

    matrix[m - 1][n] = 1
    for row in range(m-1, -1, -1):
        for col in range(n-1, -1, -1):
            if obstacleGrid[row][col] is 1:
                matrix[row][col] = 0
            else:
                matrix[row][col] = matrix[row][col + 1] + matrix[row + 1][col]

    return matrix[0][0]


query = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print "The number of unique paths possible are :", uniquePathsWithObstacles(query)