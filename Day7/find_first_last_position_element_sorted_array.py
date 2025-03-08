nums = [5,7,7,8,8,10]
target = 8

def search_range(nums,target):
    def find_position(nums, target, first):
        left, right = 0, len(nums) - 1
        position = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                position = mid
                if first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return position

    first_pos = find_position(nums, target, first=True)
    last_pos = find_position(nums, target, first=False)
    return [first_pos, last_pos]

print(search_range(nums, target))