s = "abcabc"

def count_substrings(s):

    countA = countB = countC = 0
    left = 0
    res = 0
    n = len(s)

    for right in range(n):
        if s[right] == 'a':
            countA += 1
        elif s[right] == 'b':
            countB += 1
        elif s[right] == 'c':
            countC += 1

        while countA > 0 and countB > 0 and countC > 0:
            res += (n - right)

            if s[left] == 'a':
                countA -= 1
            elif s[left] == 'b':
                countB -= 1
            elif s[left] == 'c':
                countC -= 1
            left += 1

    return res

print(count_substrings(s))
