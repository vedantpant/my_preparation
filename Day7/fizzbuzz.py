n = 10


def fizz_buzz(n):
    result = []
    # for i in range(1, n + 1):
    #     if i % 3 == 0 and i % 5 == 0:
    #         result.append("Fizzbuzz")
    #     elif i % 3 == 0:
    #         result.append("Fizz")
    #     elif i % 5 == 0:
    #         result.append("Buzz")
    #     else:
    #         result.append(str(i))
    #
    # return result
    for i in range(1, n + 1):
        str1 = ""
        if i % 3 == 0:
            str1 += "Fizz"
        elif i % 5 == 0:
            str1 += "Buzz"
        elif not str1:
            str1 += str(i)
        result.append(str1)

    return result


print(fizz_buzz(n))
