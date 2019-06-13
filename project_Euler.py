# If we list all the natural numbers below 10 that are multiples of
# 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.


def sum_natural():
    sum_num = 0
    for i in range(0, 1000):
        if i % 3 == 0:
            sum_num += i
        elif i % 5 == 0:
            sum_num += i

    return sum_num


print(sum_natural())
