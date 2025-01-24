str1 = "computer"
str2 = "cat"

def remove_first_occurance(str1, str2):
    for char in str1:
        if char in str2:
            str1 = str1.replace(char, '', 1)
            break

    return str1

print(remove_first_occurance(str1, str2))