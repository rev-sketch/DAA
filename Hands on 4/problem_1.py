'''Problem 1: Merge K Arrays (Min Heap)'''

def merge_sorted_arrays(arrays):
    result = []
    index = [0] * len(arrays)

    while True:
        min_value = None
        min_index = None

        for i, arr in enumerate(arrays):
            if index[i] < len(arr):
                if min_value is None or arr[index[i]] < min_value:
                    min_value = arr[index[i]]
                    min_index = i

        if min_value is None:
            break

        result.append(min_value)
        index[min_index] += 1

    return result

K = int(input("Enter the number of arrays (K): "))
N = int(input("Enter the size of each array (N): "))

arrays = []
for i in range(K):
    array = list(map(int, input(f"Enter elements for array {i + 1}: ").split()))
    arrays.append(array)

merged_array = merge_sorted_arrays(arrays)
print("Merged sorted array:", merged_array)

#Example 1
#Enter the number of arrays (K): 3
#Enter the size of each array (N): 4
#Enter elements for array 1: 1 3 5 7
#Enter elements for array 2: 2 4 6 8
#Enter elements for array 3: 0 9 10 11
#Merged sorted array: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

#Example 2
#Enter the number of arrays (K): 3
#Enter the size of each array (N): 3
#Enter elements for array 1: 1 3 7
#Enter elements for array 2: 2 4 8
#Enter elements for array 3: 9 10 11
#Merged sorted array: [1, 2, 3, 4, 7, 8, 9, 10, 11]
