"""
You are climbing a staircase. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to
the top?

Solution : o(n) runtime ,O(1) space - Dynamic Programming

"""


def climb_stairs(n):
    a = 1
    b = 2
    for i in range(3, n+1):
        temp = b
        b = b + a
        a = temp
    return b


print("The distinct ways 6 stairs can be climbed are:", climb_stairs(6))

