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

arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]


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

# S = "zero four zero one"
#
# def convert_word_numeric_word(S):
#
#     word_dict = {
#         "one" : 1,
#         "two" : 2,
#         "three" : 3,
#         "four" : 4,
#         "five" : 5,
#         "six" : 6,
#         "seven" : 7,
#         "eight" : 8,
#         "nine" : 9,
#         "zero" : 0
#     }
#
#     numeric_word = ""
#     word_split = S.split()
#     for word in word_split:
#         numeric_word += str(word_dict[word])
#
#     return numeric_word
#
# print(convert_word_numeric_word(S))

# s= 'geeksforgeeks is best for geeks'
# w= 'best'
#
# index = 0
# sentence = s.split()
# for i, word in enumerate(sentence):
#     if word == w:
#         index = i + 1
#         break
#
# print(index)

# from abc import ABC, abstractmethod
#
# class Polygon(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Rectangle(Polygon):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# class Triangle(Polygon):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def area(self):
#         return 0.5 * self.base * self.height
#
# rect = Rectangle(10,20)
# tria = Triangle(25,30)
# print(f"rect area:{rect.area()}")
# print(f"tria area:{tria.area()}")
# import pytest
# class BankAccount:
#
#     def __init__(self,account_number, balance=0):
#         self.__account_number = account_number
#         self.__balance = balance
#
#     def deposit(self,amount):
#         if amount > 0:
#             self.__balance += amount
#             return True
#         return False
#
#     def withdraw(self, amount):
#         if 0 < amount < self.__balance:
#             self.__balance -= amount
#             return True
#         return False
#
#     def get_balance(self):
#         return self.__balance
#
# account = BankAccount("123234325489", 5000)
# print(account.deposit(500))
# print(account.withdraw(200))
# print(account.get_balance())
#
# @pytest.fixture
# def bank_account():
#     return BankAccount("12343434", 1000)
#
# def test_deposit(bank_account):
#     assert bank_account.deposit(500)
#     assert bank_account.get_balance() == 1500
#
# def test_withdrawal(bank_account):
#     assert bank_account.withdraw(200)
#     assert bank_account.get_balance() == 800
#
# def test_withdrawal_with_insufficient_balance(bank_account):
#     assert bank_account.withdraw(2000) is False
# import unittest
# class Vehicle:
#
#     def __init__(self, brand):
#         self.brand = brand
#
#     def display_info(self):
#         return f"Vehicle Brand: {self.brand}"
#
# class Car(Vehicle):
#
#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model
#
#     def display_info(self):
#         return f"Car Brand: {self.brand}, Model: {self.model}"
#
# class TestCar(unittest.TestCase):
#     def setUp(self):
#         """Set up a Car instance before each test."""
#         self.car = Car("Toyota", "Corolla")
#
#     def test_car_display_info(self):
#         """Test the display_info method."""
#         expected_output = "Car Brand: Toyota, Model: Corolla"
#         self.assertEqual(self.car.display_info(), expected_output)
#
# if __name__ == "__main__":
#     unittest.main()

# class Animal:
#
#     def make_sound(self):
#         return "Some generic sound"
#
# class Dog(Animal):
#     def make_sound(self):
#         return "Woof!"
#
# class Cat(Animal):
#     def make_sound(self):
#         return "Meow!"
#
# animals = [Dog(), Cat(), Animal()]
# for animal in animals:
#     print(animal.make_sound())

# from abc import ABC, abstractmethod
# import math
#
# class Shape(ABC):
#
#     @abstractmethod
#     def area(self):
#         pass
#
# class Rectangle(Shape):
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
# rect = Rectangle(5, 10)
# circle = Circle(8)
#
# print(rect.area())
# print(circle.area())
#
# import unittest
#
# class TestRectangle(unittest.TestCase):
#     def setUp(self):
#         """Set up a Rectangle instance before each test."""
#         self.rect = Rectangle(10, 5)
#
#     def test_rectangle_area(self):
#         """Test the area calculation method."""
#         self.assertEqual(self.rect.area(), 50)  # ✅ Correct assertion
#
#     def test_rectangle_area_float(self):
#         """Test area with floating-point values."""
#         rect = Rectangle(14.2, 14.17)
#         self.assertAlmostEqual(rect.area(), 201.0619, places=0)  # ✅ Handles float precision
#
# if __name__ == "__main__":
#     unittest.main()

# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius
#
#     @property
#     def radius(self):
#         return self.__radius
#
#     @radius.setter
#     def radius(self, value):
#         if value >= 0:
#             self.__radius = value
#         else:
#             print("Radius cannot be negative")
#
#     def area(self):
#         return 3.14159 * self.__radius ** 2
#
# circle = Circle(5)
# print("Area:", circle.area())
# circle.radius = -10
# print("radius:", circle.radius)

# class Vehicle:
#     pass
#
# car = Vehicle
# car.wheels = 4
# car.make = "Toyota"
# car.model = "camery"
#
# print(f"car:{car.make} {car.model}")

# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#
#     @abstractmethod
#     def area(self):
#         pass
#
#     def perimeter(self):
#         pass
#
#
# class Rectangle(Shape):
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#
# class Circle(Shape):
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def perimeter(self):
#         return 2 * 3.14 * self.radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
# rectangle = Rectangle(10, 20)
# circle = Circle(5)
# print("Rectangle:", rectangle.area(), rectangle.perimeter())
# print("Circle:", circle.area(), circle.perimeter())

# class Author:
#     def __init__(self, name):
#         self.name = name
#
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = Author(author)
#
#     def display(self):
#         print(f"Book: {self.title}, Author:{self.author}")
#
# book = Book("Python Programming", "John Doe")
# book.display()

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
# v1 = Vector(2, 4)
# v2 = Vector(3, 6)
# print("Vector Addition:", v1 + v2)

# class Calculator:
#     @staticmethod
#     def add(a, b):
#         return a + b
#
#     @classmethod
#     def multiply(cls, a, b):
#         return a * b
#
# print("Addition:", Calculator.add(2 ,3))
# print("Multiplication:",Calculator.multiply(2, 4))

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self.__name = value
        else:
            print("Invalid name")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 0:
            self.__age = value
        else:
            print("Invalid age")

person = Person("vedant pant", 28)
print("Name:", person.name)
print("Age:", person.age)
person.name = ""
person.age = -10