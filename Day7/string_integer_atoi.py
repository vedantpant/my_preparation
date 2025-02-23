s = "4193 with words."

def convert_str_to_int(s):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    s = s.strip()

    if not s:
        return 0

    sign = 1
    if s[0] in ("+","-"):
        if s[0] == "-":
            sign = -1
        s = s[1:]

    num = 0
    for char in s:
        if not char.isdigit():
            break
        num = num * 10 + int(char)

    num *= sign
    if num > INT_MAX: return INT_MAX
    if num < INT_MIN: return INT_MIN

    return num

print(convert_str_to_int(s))