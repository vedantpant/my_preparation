str1 = "bbbbaaaaabbabababa"
k = 5

def maximum_occurring_string(string,k):
    curr = ""
    n = len(str1)
    i = j = 0

    mp = {}

    while j < n:
        curr += string[j]

        if j - i + 1 < k:
            j += 1

        elif j- i + 1 == k:
            if curr in mp:
                mp[curr] += 1
            else:
                mp[curr] = 1
            curr = curr[1:]
            i += 1
            j += 1

    cnt = -1
    ans = ""
    for x in mp:
        c = mp[x]
        if c > cnt or (c == cnt and x < ans):
            ans = x
            cnt = c

    return ans,cnt

print(maximum_occurring_string(str1, k))

