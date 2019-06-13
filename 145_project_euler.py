

def find_reverse():
    count_num = 0
    for i in range(1000):
        str_num = str(i)
        str_rev = str(i)[:: -1]
        if str_num[0] != "0" and str_rev[0] != "0":
            if (int(str_num) + int(str_rev)) % 2 != 0:
                count_num += 1
            else:
                i += 1
        else:
            i += 1

    return count_num


print(find_reverse())
