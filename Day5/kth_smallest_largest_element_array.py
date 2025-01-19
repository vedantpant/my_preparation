nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
import heapq


def kth_largest_element(nums, k):
    #     n = len(arr)
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             if arr[i] > arr[j]:
    #                 arr[i], arr[j] = arr[j], arr[i]
    #
    #     return arr[n - k]

    # quick select
    #     k = len(arr) - k
    #
    #     def quickselect(l, r):
    #         pivot, p = arr[r], l
    #         for i in range(l,r):
    #             if arr[i] <= pivot:
    #                 arr[i], arr[p] = arr[p], arr[i]
    #                 p += 1
    #         arr[p], arr[r] = arr[r], arr[p]
    #
    #         if p > k: return quickselect(l, p-1)
    #         elif p < k: return quickselect(p+1, r)
    #         else: return arr[p]
    #     return quickselect(0, len(arr) - 1)

    # n = len(nums)
    # # max heap formula
    # for i in range(n):
    #     nums[i] = -nums[i]
    #
    # heapq.heapify(nums)
    #
    # for _ in range(k-1):
    #     heapq.heappop(nums)
    #
    # return -heapq.heappop(nums)

    # min heap
    min_heap = []
    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        else:
            heapq.heappushpop(min_heap, num)
    return min_heap[0]

print(kth_largest_element(nums, k))
