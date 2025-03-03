nums1 = {1,2,3}
nums2 = {4,2,5}
nums3 = {3,2,6}

def two_out_of_three(nums1, nums2, nums3):

    set1, set2, set3 = set(nums1), set(nums2), set(nums3)

    result = (set1 & set2) | (set3 & set1) | (set2 & set3)

    return list(result)

print(two_out_of_three(nums1, nums2, nums3))