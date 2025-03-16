# arr = [1,2,4,5,6]
#
# def find_missing_number(arr):
#     n= len(arr) + 1
#     expected_sum = n * (n + 1) // 2
#     actual_sum = sum(arr)
#     return expected_sum - actual_sum
#
# print(find_missing_number(arr))
# arr = [1,2,3,4,5]
# k = 2
#
# def rotate_an_array(arr, k):
#     n = len(arr)
#     k = k % n
#     return arr[-k:] + arr[:-k]
#
# print(rotate_an_array(arr,k))
# str = "madam"
#
# def is_palindrome(str):
#     left, right = 0 , len(str) - 1
#     while left < right:
#         if str[left] != str[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
#
# print(is_palindrome(str))
# str = "swiss"
# def first_non_repeating_char(str):
#     char_count = {}
#
#     for char in str:
#         char_count[char] = char_count.get(char, 0) + 1
#
#     for char in str:
#         if char_count[char] == 1:
#             return char
#
#     return None
#
# print(first_non_repeating_char(str))

# class List_Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# def reverse_linked_list(head):
#     prev = None
#     current = head
#     while current:
#         next_node = current.next
#         current.next = prev
#         prev = current
#         current = next_node
#
#     return prev
#
# def print_list(head):
#     while head:
#         print(head.val, end=" -> ")
#         head = head.next
#     print("None")
#
# head = List_Node(1, List_Node(2, List_Node(3, List_Node(4, List_Node(5)))))
# print(head)
# print_list(head)
#
# reversed_head = reverse_linked_list(head)
# print("Reversed List:")
# print_list(reversed_head)

# def merge_sorted_arr(arr1, arr2):
#     i, j = 0, 0
#     merged = []
#
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             merged.append(arr1[i])
#             i += 1
#         else:
#             merged.append(arr2[j])
#             j += 1
#
#     merged.extend(arr1[i:])
#     merged.extend(arr2[j:])
#
#     return merged
#
# arr1 = [1, 3, 5, 7]
# arr2 = [2, 4, 6, 8]
#
# print(merge_sorted_arr(arr1, arr2))

# class StackArray:
#
#     def __init__(self):
#         self.stack = []
#
#     def push(self, value):
#         self.stack.append(value)
#
#     def pop(self):
#         if self.is_empty():
#             return "stack is empty"
#         return self.stack.pop()
#
#     def peek(self):
#         if self.is_empty():
#             return "stack is empty"
#         return self.stack[-1]
#
#     def is_empty(self):
#         return len(self.stack) == 0
#
#     def size(self):
#         return len(self.stack)
#
# stack = StackArray()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.peek())  # Output: 3
# print(stack.pop())  # Output: 3
# print(stack.size())  # Output: 2

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
# class StackedLinkedList:
#     def __init__(self):
#         self.head = None
#
#     def push(self,value):
#         new_node = Node(value)
#         new_node.next = self.head
#         self.head = new_node
#
#     def pop(self):
#         if self.is_empty():
#             return None
#         value = self.head.value
#         self.head = self.head.next
#         return value
#
#     def peek(self):
#         if self.is_empty():
#             return "stack is empty"
#         return self.head.value
#
#     def is_empty(self):
#         return self.head is None

# arr = [1, 1, 2, 2, 3, 4, 4, 5]
#
# def remove_duplicate(arr):
#
#     if not arr:
#         return 0
#
#     unique_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] != arr[unique_index]:
#             unique_index += 1
#             arr[unique_index] = arr[i]
#
#     return unique_index + 1
#
# new_length = remove_duplicate(arr)
# print(arr[:new_length])

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
# def has_cycle(head):
#     fast = head
#     slow = head
#
#     while fast and fast.next:
#         fast = fast.next.next
#         slow = slow.next
#
#         if fast == slow:
#             return True
#
#     return False
#
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
#
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node2
#
# print(has_cycle(node1))

# class ListNode:
#
#     def  __init__(self, value):
#         self.value = value
#         self.next = None
#
# def get_intersection_node(headA, headB):
#     if not headA or not headB:
#         return None
#
#     ptrA, ptrB = headA, headB
#
#     while ptrA != ptrB:
#         ptrA = ptrA.next if ptrA else headB
#         ptrB = ptrB.next if ptrB else headA
#
#     return ptrA
#
# common = ListNode(8)
# common.next = ListNode(10)
#
# headA = ListNode(3)
# headA.next = ListNode(6)
# headA.next.next = common
#
# headB = ListNode(5)
# headB.next = common
#
# intersection = get_intersection_node(headA, headB)
# print(intersection.value if intersection else "no intersection")

# nums = [1, 3, 5, 7, 9, 11]
# target = 7
#
# def binary_search(nums, target):
#     left, right = 0 , len(nums) - 1
#
#     while left <= right:
#         mid = (left +right) // 2
#
#         if nums[mid] == target:
#             return mid
#
#         elif nums[mid] < target:
#             left = mid + 1
#
#         else:
#             right = mid - 1
#
#     return -1
#
# print(binary_search(nums,target))

# import heapq
#
# arr = [7, 10, 4, 3, 20, 15]
# k = 3
#
# def find_kth_smallest(nums,k):
#     return heapq.nsmallest(k, arr)[-1]
#
# def find_kth_largest(nums, k):
#     return heapq.nlargest(k, arr)[-1]
#
# print(find_kth_smallest(arr, k))
# print(find_kth_largest(arr, k))

# def longest_common_subsequence(X,Y):
#     m,n = len(X), len(Y)
#     dp = [[0] * (n + 1) for _ in range(m + 1)]
#
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             if X[i - 1] == Y[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1] + 1
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#
#     return dp[m][n]
#
# X = "AGGTAB"
# Y = "GXTXAYB"
#
# print("Length of LCS", longest_common_subsequence(X, Y))

# nums = [10, 20, 4, 45, 99, 99]
#
# def second_largest(nums):
#     if len(nums) < 2:
#         return "Array must have more than two elements"
#
#     first = second = float("-inf")
#
#     for num in nums:
#         if num > first:
#             second = first
#             first = num
#         elif second < num < first:
#             second = num
#
#     return second if second != float("-inf") else "no second largest number."
#
# print("Second Largest:", second_largest(nums))

# arr = [2, 7, 4, 8, -1, 3, 1, 5]
# target = 6
# def find_pair(arr, target):
#     seen = set()
#     pairs = []
#
#     for num in arr:
#         complement = target - num
#         if complement in seen:
#             pairs.append((complement, num))
#         seen.add(num)
#
#     return pairs
#
# print("Pairs",find_pair(arr, target))

# def are_anagram_sorting(s1, s2):
#     if len(s1) != len(s2):
#         return False
#
#     count = [0] * 26
#
#     for c1, c2 in zip(s1, s2):
#         count[ord(c1) - ord("a")] += 1
#         count[ord(c2) - ord("a")] -= 1
#
#     return all(x == 0 for x in count)
#
# print(are_anagram_sorting("listen", "silent"))
# print(are_anagram_sorting("hello", "world"))"

# def length_of_longest_substring(s):
#     char_index = {}
#     left = 0
#     max_length = 0
#
#     for right, char in enumerate(s):
#         if char in char_index and char_index[char] >= left:
#             left = char_index[char] + 1
#         else:
#             char_index[char] = right
#             max_length = max(max_length, right - left + 1)
#
#     return max_length

# s = "hello"
#
# def reverse_vowels(s):
#     vowels = set("aeiouAEIOU")
#     s = list(s)
#
#     left, right = 0, len(s) - 1
#     while left < right:
#         if s[left] not in vowels:
#             left += 1
#         elif s[right] not in vowels:
#             right -= 1
#         else:
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1
#
#     return "".join(s)
#
# print(reverse_vowels("hello"))

# nums = [-1,0,1,2,-1,-4]
#
# def three_sum(nums):
#     nums.sort()
#     result = []
#
#     for i in range(len(nums) - 2):

# def find_min(nums):
#     left, right = 0, len(nums) -1
#
#     while left < right:
#         mid = (left + right) // 2
#
#         if nums[mid] > nums[right]:
#             left = mid + 1
#         else:
#             right = mid
#
#     return nums[left]
#
# print(find_min([3,4,5,1,2]))

# nums = [2,3,-2,4]
#
# def max_Product(nums):
#     if not nums:
#         return 0
#
#     max_product = min_product = result = nums[0]
#
#     for i in range(1, len(nums)):
#         num = nums[i]
#
#         if num < 0:
#             max_product, min_product = min_product, max_product
#
#         max_product = max(num, max_product * num)
#         min_product = min(num, min_product * num)
#
#         result = max(result, max_product)
#
#     return result
#
# print(max_Product(nums))

# def max_subarray(nums):
#     max_sum = float("-inf")
#     curr_sum = 0
#
#     for num in nums:
#         curr_sum += num
#         max_sum = max(max_sum, curr_sum)
#
#         if curr_sum < 0:
#             curr_sum = 0
#
#     return max_sum
#
# print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))

# numbers = [2, 7, 11, 15]
# target = 9
# def two_sum_2(numbers, target):
#     left, right = 0, len(numbers) - 1
#
#     while left < right:
#         current_sum = numbers[left] + numbers[right]
#
#         if current_sum == target:
#             return [left + 1, right + 1]
#
#         elif current_sum < target:
#             left += 1
#
#         else:
#             right -= 1
#
#     return []
#
# print(two_sum_2(numbers, target))

# s = "hello world"
# def reverse_words(s):
#     s = s.strip()
#     words = s.split()
#     words.reverse()
#
#     return " ".join(words)
#
# print(reverse_words(s))