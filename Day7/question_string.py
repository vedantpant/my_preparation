test_list1 = ["Gfg", "is", "best"]
test_list2 = ["I love Gfg", "Its Best for Geeks", "Gfg means CS"]

res = []
for l1 in test_list1:
    temp = False
    for l2 in test_list2:
        if l1 in l2:
            print(f"'{l1}' found in '{l2}'")
            temp = True
            break
    res.append(temp)

print(f"the result {res}")

