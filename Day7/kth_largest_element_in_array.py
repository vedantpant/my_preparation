import heapq

def find_kth_largest(nums, k):
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappushpop(min_heap, num)

    return min_heap[0]

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(find_kth_largest(nums, k))