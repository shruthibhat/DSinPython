"""
You are climbing a staircase. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to
the top?

Solution : o(n) runtime ,O(1) space - Dynamic Programming

"""
__author__ = "Shruthi"


def climb_stairs(n):
    if n == 1:
        return 1
    a = 1
    b = 2
    for i in range(3, n+1):
        temp = b
        b = b + a
        a = temp
    return b


if __name__ == '__main__':
    print("The distinct ways 1 stairs can be climbed are:", climb_stairs(1))
    print("The distinct ways 2 stairs can be climbed are:", climb_stairs(2))
    print("The distinct ways 6 stairs can be climbed are:", climb_stairs(6))

