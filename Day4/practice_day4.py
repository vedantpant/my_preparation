# # find the first non-repeating character in a string
#
# str1 = "bhavay"
#
#
# def find_first_non_repeating(str1):
#     count = {}
#     for char in str1:
#         if char in count:
#             count[char] += 1
#         else:
#             count[char] = 1
#
#     for char in count:
#         if count[char] == 1:
#             return char
#
#
# print(find_first_non_repeating(str1))


# arr1 = [10, 4, 5, 67, 8, 9, 321, 45, 6, 54]
#
#
# def second_largest_number(arr1):
#     if len(arr1) < 2:
#         return None
#     largest = second = float("-inf")
#
#     for num in arr1:
#         if num > largest:
#             second = largest
#             largest = num
#         elif num > second and num != largest:
#             second = num
#
#     return second if second != float("-inf") else None
#
# print(second_largest_number(arr1))

# arr1 = [0, 1, 0, 1, 0, 1, 1, 0, 1, 0]
#
#
# def segregate_0_1(arr1):
#     n = len(arr1)
#     count = 0
#     for num in arr1:
#         if num == 0:
#             count += 1
#
#     for i in range(count):
#         arr1[i] = 0
#
#     for i in range(count,n):
#         arr1[i] = 1
#
#     return arr1
#
#
# print(segregate_0_1(arr1))

# display the longest name

# names_list = ["Alice", "Bob", "Catherine", "Elizabeth", "John"]
#
#
# def longest_name(name_list):
#     if not name_list:
#         return None
#     return max(name_list, key=len)
#
#
# print(longest_name(names_list))

# arr1 = [20, 10, 20, 4, 100]
#
#
# def find_largest(arr1):
#     max = arr1[0]
#     n = len(arr1)
#     for i in range(1, n):
#         if arr1[i] > max:
#             max = arr1[i]
#
#     return max
#
#
# print(find_largest(arr1))

# n = 5
#
# def square_sum(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += i ** 2
#
#     return sum
#
# print(square_sum(n))

arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
k = 2


def rotate_left(arr1, k):
    n = len(arr1)
    k = k % n
    return arr1[k:] + arr1[:k]

def rotate_right(arr1, k):
    n = len(arr1)
    k = k % n
    return arr1[-k:] + arr1[:-k]


print(rotate_left(arr1, k))
print(rotate_right(arr1, k))
