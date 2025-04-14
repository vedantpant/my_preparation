needle = "sad"
haystack = "sadbutsad"

def find_index_of_first_occurrence(needle, haystack):
    n, m = len(haystack), len(needle)

    for i in range(n-m+1):
        if haystack[i:i+m] == needle:
            return i
    return -1

print(find_index_of_first_occurrence(needle, haystack))