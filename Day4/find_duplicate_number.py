num = [3,1,3,4,2]

# def duplicate_number(num):
#     n = len(num)
#     for i in range(n):
#         for j in range(i+1,n):
#             if num[i] == num[j]:
#                 return num[i]
#
#
# print(duplicate_number(num))


# floyds tortoise and hares

def find_duplicate_number(num):
    slow, fast = 0

    while True:
        slow = num[slow]
        fast = num[num[fast]]

        if slow == fast:
            break

