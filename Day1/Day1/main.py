# Integer
# print(8)
# print(1e309)
#
# # Decimal/Float
# print(8.55)
# print(1.7e309)
#
# # Boolean
# print(True)
# print(False)
#
# # Text/String
# print('Hello World')
#
# # complex
# print(5+6j)
#
# # List-> C-> Array
# print([1,2,3,4,5])
#
# # Tuple
# print((1,2,3,4,5))
#
# # Sets
# print({1,2,3,4,5})
#
# # Dictionary
# print({'name':'Nitish','gender':'Male','weight':70})
#
# # type
# type([1,2,3])
#
# a = 5
# print(type(a))
#
# b = str(a)
# print(type(b))
#
# a = 0b1010 #Binary Literals
# b = 100 #Decimal Literal
# c = 0o310 #Octal Literal
# d = 0x12c #Hexadecimal Literal
#
# #Float Literal
# float_1 = 10.5
# float_2 = 1.5e2 # 1.5 * 10^2
# float_3 = 1.5e-3 # 1.5 * 10^-3
#
# #Complex Literal
# x = 3.14j
#
# print(a, b, c, d)
# print(float_1, float_2,float_3)
# print(x, x.imag, x.real)
#
# string = 'This is Python'
# strings = "This is Python"
# char = "C"
# multiline_str = """This is a multiline string with more than one line code."""
# unicode = u"\U0001f600\U0001F606\U0001F923"
# raw_str = r"raw \n string"
#
# print(string)
# print(strings)
# print(char)
# print(multiline_str)
# print(unicode)
# print(raw_str)
#
# # Arithmetric Operators
# print(5 - 6)  # Corrected expression
# print(5 * 6)  # Corrected expression
# print(5 / 2)  # Corrected expression
# print(5 // 2)  # Corrected expression
# print(5 % 2)  # Corrected expression
# print(5 ** 2)  # Corrected expression
#
# # Relational Operators
# print(4 > 5)  # Corrected expression
# print(4 < 5)  # Corrected expression
# print(4 >= 4)  # Corrected expression
# print(4 <= 4)  # Corrected expression
# print(4 == 4)  # Corrected expression
# print(4 != 4)  # Corrected expression
#
# # Logical Operators
# print(1 and 0)  # Corrected expression
# print(1 or 0)  # Corrected expression
# print(not 1)  # Corrected expression
#
# # Bitwise Operators
#
# # bitwise and
# print(2 & 3)  # Corrected expression
# # bitwise or
# print(2 | 3)  # Corrected expression
#
# # bitwise xor
# print(2 ^ 3)  # Corrected expression
# print(~3)  # Corrected expression
# print(4 >> 2)  # Corrected expression
# print(5 << 2)  # Corrected expression
#
# # Assignment Operators
# a = 2
# a %= 2
# print(a)  # Corrected expression
#
# # Membership Operators
# # in/not in
# print('D' not in 'Delhi')  # Corrected expression
# print(1 in [2, 3, 4, 5, 6])  # Corrected expression

# curre_population = 100000
# growth_rate = 1.1
# for i in range(10, 0,-1):
#     curre_population = curre_population * growth_rate
#     print(f"Population after {i} years is {curre_population}")

# n = int(input("Enter the value of n:"))
#
# fact = 1
# result = 0
#
# for i in range(1, n+1):
#     fact = fact * i
#     result += i/fact
#
# print(result)

# for i in range(5):
#     for j in range(i+1):
#         print("*", end=" ")
#     print(" ")


for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    for k in range(i-1, 0, -1):
        print(k, end="")
    print(" ")

