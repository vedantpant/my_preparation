# #
# #
# # def counting_odd_even(ls1):
# #     n = len(ls1)
# #     even_count = 0
# #     odd_count = 0
# #     for i in range(n):
# #         if ls1[i] % 2 == 0:
# #             even_count += 1
# #         else:
# #             odd_count += 1
# #
# #     return even_count, odd_count
# #
# #
# # even_count, odd_count = counting_odd_even(ls1)
# # print(even_count, odd_count)
#
#
# Given an array, the task is to find average of that array. Average is the
# sum of array elements divided by the number of elements.

# def find_average(ls1):
#     return sum(ls1) / len(ls1)
#
# # Testing the function
# print(find_average(ls1))

# ch = "vedant is awesome"
#
# def count_vowels(ch):
#     count = 0
#     vowels = ["a", "e", "i", "o", "u"]
#     for char in ch:
#         if char.lower() in vowels:
#             count += 1
#
#     return count
#
# print(count_vowels(ch))

# arr1 = [1, 2, 3, 3, 4, 4, 3, 5, 6, 5, 6, 5, 6, 5, 5, 6]

# def repeating_numbers(arr1):
#     count_dict = {}
#     for num in arr1:
#         if num in count_dict:
#             count_dict[num] += 1
#         else:
#             count_dict[num] = 1
#
#     repeating_nums = []
#     for num, count in count_dict.items():
#         if count > 1:
#             repeating_nums.append(num)
#
#     return repeating_nums
#
# print(repeating_numbers(arr1))

# n = 1234


# def is_palindrome(n):
#     rever_n = str(n)[::-1]
#     if int(rever_n) == n:
#         return True
#     else:
#         return False
#
#
# print(is_palindrome(n))

# def check_status(a, b, flag):
#
#     if a > 0 or b > 0 and flag == False:
#         return True
#     elif a < 0 and b < 0 and flag == True:
#         return True
#     else:
#         return False
#
#
# print(check_status(5, 3, True))

# def is_perfect_square(x):
#     low, high = 1, x
#     while low <= high:
#         mid = (low + high) // 2
#         square = mid * mid
#         if square == x:
#             return True
#         elif square < x:
#             low = mid + 1
#         else:
#             high = mid - 1
#
#     return False
#
#
# print(is_perfect_square(56))


# arr1 = [x for x in range(20)]
# # find the 13 number in the above array
#
#
# def find_a_number(arr1):
#     target = 30
#     low = 0
#     high = len(arr1) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr1[mid] == target:
#             return mid
#         elif arr1[mid] < target:
#             low = mid + 1
#         elif arr1[mid] > target:
#             high = mid - 1
#
#     return -1
#
#
# print(find_a_number(arr1))

# n = 687
#
#
# def find_digit_sum(n):
#     digit_sum = 0
#     while n > 0:
#         digit_sum += n % 10
#         n //= 10
#
#     return digit_sum
#
#
# print(find_digit_sum(123))

# n = 3
#
# def difference_sum(n):
#     sum1 = 0
#     sum2 = 0
#     for i in range(n+1):
#         sum1 += i
#         sum2 += i ** 2
#
#     return sum1 ** 2 - sum2
#
#
# print(difference_sum(n))

# import math
#
# n = 153
#
# def armstrong(n):
#     number = str(n)
#
#     n = len(number)
#     output = 0
#     for i in range(n):
#         output += int(number[i]) ** n
#
#     if output == int(number):
#         return True
#     else:
#         return False
#
#
# arm_list = []
#
# for i in range(1, 1000):
#     if armstrong(i):
#         arm_list.append(i)
#
# print(f"arm_list: {arm_list}")

# def factorial(number):
#     if number == 0:
#         return 1
#     else:
#         return number * factorial(number - 1)
#
# print(factorial(10))

# def factorial(number):
#     fact = 1
#     for i in range(2, number+1):
#         fact *= i
#     return fact
#
# print(factorial(5))

# arr = [20, 21, 45, 1, 89, 89, 90]
#
#
# def sorted_or_not(arr, n):
#     if n == 0 or n == 1:
#         return True
#     for i in range(1, n):
#         if arr[i - 1] > arr[i]:
#             return False
#     return True
#
#
# print(sorted_or_not(arr, len(arr)))

# n = 5
#
#
# def mult_table(n):
#     for i in range(1, 11):
#         print(f"{n} * {i} = {n * i}")
#
#
# mult_table(n)

# str = "Geeks for Geeks"
# word = "eeks"
#
# sentence = str.split(" ")
# print(sentence)
#
# if word in sentence:
#     print("yes")
# else:
#     print("no")

# arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
#
#
# def segregate0and1(arr):
#     n = len(arr)
#     count = 0
#     for i in range(n):
#         if arr[i] == 0:
#             count += 1
#
#     for i in range(count):
#         arr[i] = 0
#
#     for i in range(count,n):
#         arr[i] = 1
#
#     return arr
#
#
# print(segregate0and1(arr))

# arr = [0, 1, 2, 0, 1, 2]
#
#
# def sort_arr_ascending(arr):
#     n = len(arr)
#     count1 = 0
#     count2 = 0
#     for i in range(n):
#         if arr[i] == 0:
#             count1 += 1
#         elif arr[i] == 1:
#             count2 += 1
#
#     for i in range(n):
#         if i < count1:
#             arr[i] = 0
#         elif i < count1 + count2:
#             arr[i] = 1
#         else:
#             arr[i] = 2
#
#     return arr
#
# print(sort_arr_ascending(arr))

# def is_prime(n):
#     if n <= 1:
#         return False
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#             else:
#                 return True
#
# print(is_prime(10))

# import copy
#
# original_list = [[1, 2, 3], [4, 5, 6]]
# shallow_copy = copy.copy(original_list)
# shallow_copy[0][0] = 99
# print("Original List (After Shallow Copy Modification):", original_list)
#
# # Deep Copy Example
# deep_copy = copy.deepcopy(original_list)
# deep_copy[0][0] = 42
# print("Deep Copy List:", deep_copy)
# print("Original List (After Deep Copy Modification):", original_list)

# def simple_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before function execution")
#         func(*args, **kwargs)
#         print("After function execution")
#
#     return wrapper
#
#
# @simple_decorator
# def say_hello():
#     print("Hello, World!")
#
# say_hello()

# import requests
#
#
# class APIClient:
#
#     def __init__(self, base_url):
#         self.base_url = base_url
#
#     def get(self,endpoint, params=None):
#         response = requests.get(f"{self.base_url}/{endpoint}", params=params)
#         return response.json()
#
#     def post(self, endpoint, data):
#         response = requests.post(f"{self.base_url}/{endpoint}", json=data)
#         return response.json()
#
#
# client = APIClient("https://jsonplaceholder.typicode.com")
# print(client.get("posts/1", params={"userId": 1}))
# print(client.post("posts", data={"title": "foo", "body": "bar", "userId": 1}))

# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
# except ValueError:
#     print("Please enter a valid number")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# else:
#     print("Result: ", result)
# finally:
#     print("Execution completed")
#
# import re
#
# log_file_path = "sample_log.txt"
# error_pattern = re.compile(r"Error: (.+)")
#
# with open(log_file_path, 'r') as file:
#     for line in file:
#         match = error_pattern.search(line)
#         if match:
#             print(f"Error_found: {match.group(1)}")


import os

directory = "./files"
for count, filename in enumerate(os.listdir(directory)):
    new_file = f"file_{count}.txt"
    os.rename(os.path.join(directory, filename), os.path.join(directory, new_file))
print("successfully renamed files")