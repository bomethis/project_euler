

def find_reverse():
    reversible_num_count = 0
    for i in range(1000):
        str_num = str(i)
        str_rev = str(i)[:: -1]
        if str_num[0] != "0" and str_rev[0] != "0":
            sum_num = int(str_num) + int(str_rev)
            sum_num_count = 0
            for j in range(len(str(sum_num))):
                if int(str(sum_num)[j]) % 2 != 0:
                    sum_num_count += 1
            if len(str(sum_num) == sum_num_count:
                reversible_num_count += 1

    return reversible_num_count


print(find_reverse())
