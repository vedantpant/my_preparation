input_list = [1, 2, 2, 5, 8, 4, 4, 8]

def count_unique(input_list):
    count_unique = {}
    count = 0
    lst = []
    for num in input_list:
        if num in count_unique:
            count_unique[num] += 1
        else:
            count_unique[num] = 1

    for num, count in count_unique.items():
        if count_unique[count] == 1:
            lst.append(num)

    return lst


print(count_unique(input_list))
