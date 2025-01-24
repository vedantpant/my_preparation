s = "car"
t = "rat"

from collections import Counter


def check_anagram(s, t):
    # return sorted(s) == sorted(t)


    # return Counter(s) == Counter(t)

    if len(s) != len(t):
        return False

    countS, countT = {},{}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    print(countS, countT)

    for c in countS:
        print(c)
        if countS[c] != countT.get(c, 0):
            return False

    return True

print(check_anagram(t, s))


