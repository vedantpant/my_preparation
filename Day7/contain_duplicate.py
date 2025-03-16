nums = [1, 2, 2, 4, 5]

def contain_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(contain_duplicate(nums))