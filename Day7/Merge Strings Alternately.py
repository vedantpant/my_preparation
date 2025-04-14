str1 = "abc"
str2 = "pqr"

def merge_alternatively(str1, str2):
    result = ""
    i, j = 0, 0

    while i < len(str1) and j < len(str2):
        result += str1[i] + str2[j]
        i += 1
        j += 1
    result += str1[i:] + str2[j:]
    return result

print(merge_alternatively(str1, str2))
