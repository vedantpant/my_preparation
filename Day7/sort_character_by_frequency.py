from collections import defaultdict

s = "tree"

def sort_by_frequency(s):

    map = {}

    for char in s:
        if char in map:
            map[char] += 1
        else:
            map[char] = 1

    buckets = defaultdict(list) # freq -> [char]
    for char, cnt in map.items():
        buckets[cnt].append(char)

    res = []
    for i in range(len(s), 0, -1):
        for ch in buckets[i]:
            res.append(ch * i)

    return "".join(res)


print(sort_by_frequency(s))