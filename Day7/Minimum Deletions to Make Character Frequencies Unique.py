s = "aaabbbcc"

def delMinimum(s):

    freq = [0] * 26

    for char in s:
        freq[ord(char) - ord('a')] += 1

    freq = sorted([f for f in freq if f > 0], reverse=True)

    used_freq = set()
    deletion = 0

    for i in range(len(freq)):
        while freq[i] > 0 and freq[i] in used_freq:
            freq[i] -= 1
            deletion += 1
        used_freq.add(freq[i])

    return deletion

print(delMinimum(s))
