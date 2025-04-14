str = "Hello World"

def length_of_last_word(str):
    return len(str.strip().split(" ")[-1])

print(length_of_last_word(str))
