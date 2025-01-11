# find a missing number from an array of 1 to n
# import pytest
#
# arr1 = [1, 2, 4, 6, 3, 7, 8]
#
#
# def find_missing_number(arr1):
#     n = len(arr1) + 1
#     print(n)
#     total = n * (n + 1) / 2
#     sum1 = sum(arr1)
#     number = total - sum1
#
#     return number
#
#
# print(find_missing_number(arr1))
#
#
# @pytest.mark.parametrize('arr1, expected', [([1, 2, 4, 6, 3, 7, 8], 5), ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)])
# def test_find_missing_number(arr1, expected):
#     assert find_missing_number(arr1) == expected

# rotate an array

arr1 = [1, 2, 3, 4, 5, 6, 7]
k = 2
#
#
# def rotate_element_right(arr1, k):
#     n = len(arr1)
#     k = k % n
#     arr1 = arr1[::-1]
#     arr1[:k] = reversed(arr1[:k])
#     arr1[k:] = reversed(arr1[k:])
#     return arr1
#
#
# print(rotate_element_right(arr1, k))

# rotate_elements by left


# def rotate_elements_left(arr1, k):
#     n = len(arr1)
#     k = k % n
#     arr1[:k] = reversed(arr1[:k])
#     arr1[k:] = reversed(arr1[k:])
#     arr1 = arr1[::-1]
#
#     return arr1
#
#
# print(rotate_elements_left(arr1, k))

# words = ["level", "hello", "world", "civic", "python", "madam"]
#
#
# def is_palindrome(words):
#     return [word for word in words if word == word[::-1]]

# print(is_palindrome(words))
