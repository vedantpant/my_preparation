def int_to_roman(int_value):
    sys_list = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100],
                ["CD", 400],["D", 500],["CM", 900],["M", 1000]]

    result = ""
    for sym, val in reversed(sys_list):
        if int_value // val:
            count = int_value // val
            result += sym * count
            int_value = int_value % val

    return result

print(int_to_roman(55))


