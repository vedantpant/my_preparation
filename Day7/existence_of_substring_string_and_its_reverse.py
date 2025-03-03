# We need to check if a given substring exists in a
# string and also in its reversed version.

s = "abba"
sub = "ab"

def exist_in_both(s, sub):
    reversed_string = s[::-1]

    return sub in s and sub in reversed_string

print(exist_in_both(s, sub))
