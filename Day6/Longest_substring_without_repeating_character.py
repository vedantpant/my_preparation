str1 ="abcabccbb"


def longest_substring(str1):

    char_set = set()
    l = 0
    res = 0
    for r in range(len(str1)):
        while str1[r] in char_set:
            char_set.remove(str1[l])
            l += 1
        char_set.add(str1[r])
        res = max(res, r - l + 1)

    return res


print(longest_substring(str1))
