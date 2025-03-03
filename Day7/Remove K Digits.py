def remove_k_digits(num, k):
    stack = []

    for c in num:
        while k > 0 and stack and stack[-1] > c:
            k -= 1
            stack.pop()
        stack.append(c)

    stack = stack[:len(stack) - k] if k > 0 else stack
    res = "".join(stack)
    return str(int(res)) if res else "0"

# Example Usage
print(remove_k_digits("1432219", 3))  # Output: "1219"
print(remove_k_digits("10200", 1))    # Output: "200"
print(remove_k_digits("10", 2))