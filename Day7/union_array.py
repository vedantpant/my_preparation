a = [85, 25, 1, 32, 54, 6]
b= [85, 2]

def  find_union_array(a, b):
    return (set(a) | set(b))

print(find_union_array(a, b))