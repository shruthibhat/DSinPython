def two_sum (A, target):
    """Returns the first positions of the first occuring elements whose sum is same as target else return 0"""
    two_sum_dict = {}
    for i,item in enumerate(A):
        if (target - item) in two_sum_dict:
            return [two_sum_dict.get(target - item) + 1, i+1]
        else:
            two_sum_dict[item] = i
    return [0, 0]


print(two_sum([2, 4, 6, 7, 8, 10], 12))
print(two_sum([2, 4, 6, 7, 8, 10], 100))