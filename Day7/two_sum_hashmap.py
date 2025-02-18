nums = [2, 1, 5, 3]
target = 4

def find_two_sum(nums, target):
    map = {}
    for num in nums:
        complement = target - num
        if complement in map:
            return [map[complement], num]
        map[num] = num

    return map

print(find_two_sum(nums, target))
