import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_idx = right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])

    return merged

def test_merge_sort(arr):
    start_time = time.time()
    sorted_arr = merge_sort(arr)
    end_time = time.time()
    runtime = end_time - start_time

    return sorted_arr, runtime


arr = [5, 2, 4, 7, 1, 3, 2, 6]
sorted_arr, runtime = test_merge_sort(arr)
print("Sorted Array:", sorted_arr)
print("Runtime:", runtime, "seconds")

'''Sorted Array: [1, 2, 2, 3, 4, 5, 6, 7]
Runtime: 2.86102294921875e-05 seconds'''

