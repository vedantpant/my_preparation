# find the first non-repeating character in a string

str1 = "bhavay"


def find_first_non_repeating(str1):
    count = {}
    for char in str1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char in count:
        if count[char] == 1:
            return char


print(find_first_non_repeating(str1))
