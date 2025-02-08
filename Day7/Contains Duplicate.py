nums = [1,2,3,1]

def find_duplicate(nums):
    # n = len(nums)

    # for i in range(n):
    #     for j in range(i+1, n):
    #         if nums[i] == nums[j]:
    #             return True
    # return False

    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

print(find_duplicate(nums))

