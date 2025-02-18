a = [1, 3, 5, 6, 3, 5, 6, 1]

b = set(a)

print(b)

prod = 0
for num in b:
    prod *= num

print(prod)