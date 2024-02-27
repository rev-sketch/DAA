import random
import timeit
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(10**6)  # Setting recursion limit higher

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def quicksort_random(arr):
    random.shuffle(arr)
    quicksort(arr, 0, len(arr) - 1)

# Benchmark functions

def generate_sorted_array(n):
    return list(range(n))

def generate_reversed_array(n):
    return list(range(n, 0, -1))

def generate_random_array(n):
    return [random.randint(1, 1000) for _ in range(n)]

def benchmark_sorting(func, array_generator, sizes, title):
    times = []
    for size in sizes:
        arr = array_generator(size)
        time = timeit.timeit(lambda: func(arr.copy(), 0, len(arr) - 1), number=1)
        times.append(time)
        print(f"Array Size: {size}")
        print(f"{title}: {time:.7f} seconds")
        print()
    plt.plot(sizes, times, label=title)

sizes = [100, 500, 1000, 2000, 5000]

# Best case
benchmark_sorting(quicksort, generate_sorted_array, sizes, "Best Case")

# Worst case
benchmark_sorting(quicksort, generate_reversed_array, sizes, "Worst Case")

# Average case
benchmark_sorting(quicksort, generate_random_array, sizes, "Average Case")

plt.xlabel('Array Size')
plt.ylabel('Time (s)')
plt.title('Non-Random Pivot Quicksort Benchmark')
plt.legend()
plt.show()

'''
Array Size: 100
Best Case: 0.0005688 seconds

Array Size: 500
Best Case: 0.0128738 seconds

Array Size: 1000
Best Case: 0.0512876 seconds

Array Size: 2000
Best Case: 0.2161600 seconds

Array Size: 5000
Best Case: 1.3419575 seconds

Array Size: 100
Worst Case: 0.0004108 seconds

Array Size: 500
Worst Case: 0.0103122 seconds

Array Size: 1000
Worst Case: 0.0350722 seconds

Array Size: 2000
Worst Case: 0.1441006 seconds

Array Size: 5000
Worst Case: 0.9057940 seconds

Array Size: 100
Average Case: 0.0000957 seconds

Array Size: 500
Average Case: 0.0004788 seconds

Array Size: 1000
Average Case: 0.0010829 seconds

Array Size: 2000
Average Case: 0.0026793 seconds

Array Size: 5000
Average Case: 0.0107068 seconds
'''