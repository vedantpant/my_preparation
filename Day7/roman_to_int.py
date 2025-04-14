def roman_to_int(s:str):
    roman_map ={
        "I":1, "IV":4, "V":5, "IX":9, "X":10, "XL":40,
         "L":50, "XC":90, "C":100, "CD":400, "D":500, "CM":900, "M":1000
         }

    result = 0

    for i in range(len(s)):
        if i+1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:
            result -= roman_map[s[i]]
        else:
            result += roman_map[s[i]]

    return result

s = "CMXCVIII"
print(roman_to_int(s))
