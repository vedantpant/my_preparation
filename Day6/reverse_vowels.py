s1 = "hello world"
s1 = list(s1)
vowels = ["a","e","i","o","u"]


def reverse_vowel(s1):
    i, j = 0, len(s1) - 1
    while i < j:
        if s1[i] in vowels and s1[j] in vowels:
            s1[i], s1[j] = s1[j], s1[i]
            i += 1
            j -= 1
        else:
            if s1[i] not in vowels:
                i += 1
            if s1[j] not in vowels:
                j -= 1

    return "".join(s1)


print(reverse_vowel(s1))



