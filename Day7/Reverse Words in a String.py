s = "let's take leetcode contest"


def reverse_words_3(s):
    t = ""
    new_sentence = []
    words = s.split()
    for word in words:
        reversed_letters = word[::-1]
        new_sentence.append(reversed_letters)
        "".join(new_sentence)
        t = " ".join(new_sentence)
    return t


print(reverse_words_3(s))  # Output: "s'teel etnoces tsetnoc nlets"




