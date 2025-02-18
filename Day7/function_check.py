# Given a string s having lowercase characters, find the length of the longest substring without repeating characters.

# Input: s = “abcdefabcbb”
# Output: 6
# Explanation: The longest substring without repeating characters is “abcdef”.

# def longest_substring(s):
#
#     map1 = {}
#     left, right = 0, 1
#     max_length = 0
#
#     while right < len(s):
#         if s[left] != s[right] and s[left] not in map1:
#             map1[s[left]] += 1
#             max_length = max(max_length, right - left + 1)
#             right += 1
#         else:
#             left += 1
#
#
#
#     return map1
#
#
# def length_of_longest_substring(s: str) -> int:
#     char_set = set()
#     left = max_length = 0
#
#     for right in range(len(s)):
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1  # Move left pointer to remove duplicates
#
#         char_set.add(s[right])
#         max_length = max(max_length, right - left + 1)  # Update max length
#
#     return max_length
#
#
# # Example Usage:
# print(length_of_longest_substring("abcabcbb"))  # Output: 3

def length_of_longest_substring(s: str) -> int:
    char_index = {}  # Dictionary to store the last index of each character
    left = max_length = 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1  # Move left pointer past the duplicate

        char_index[char] = right  # Update character's last seen index
        max_length = max(max_length, right - left + 1)  # Update max length
    return max_length





