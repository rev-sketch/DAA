import timeit as time
import random as ran
import matplotlib.pyplot as plt
import platform as pf
import psutil as psu

# System Information
def collect_system_data():
    processor_info = f"CPU: {pf.processor()}"
    
    ram_data = psu.virtual_memory()
    memory_info = f"Total Memory: {ram_data.total} bytes"

    storage_info = []
    disk_partitions = psu.disk_partitions()
    for partition in disk_partitions:
        partition_info = psu.disk_usage(partition.mountpoint)
        storage_info.append(f"{partition.device} - Total: {partition_info.total} bytes, Free: {partition_info.free} bytes")

    os_info = f"System: {pf.system()} {pf.version()}"

    return processor_info, memory_info, storage_info, os_info

# Usage
print("System Information:")
processor, memory, storage, os_data = collect_system_data()
print(processor)
print(memory)
print(os_data)
for storage_device in storage:
    print(storage_device)


# Insertion Sort
def insertion_sort(custom_array):
    for custom_i in range(1, len(custom_array)):
        custom_key = custom_array[custom_i]
        custom_j = custom_i - 1
        while custom_j >= 0 and custom_array[custom_j] > custom_key:
            custom_array[custom_j + 1] = custom_array[custom_j]
            custom_j = custom_j - 1
        custom_array[custom_j + 1] = custom_key

# Function to generate a random array of a given size
def generate_custom_array(custom_size):
    return [ran.randint(1, 1000) for _ in range(custom_size)]

# Function to benchmark sorting algorithms
def custom_benchmark(custom_sort_func, custom_array):
    custom_setup_code = f"from __main__ import {custom_sort_func}, generate_custom_array; custom_arr = generate_custom_array({len(custom_array)})"
    custom_stmt = f"{custom_sort_func}(custom_arr)"

    # Measure the execution time
    custom_exe_time = time.timeit(custom_stmt, setup=custom_setup_code, number=100)

    return custom_exe_time

# Benchmark parameters
custom_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 2500, 3000, 5000]  # Adjust as needed

# Results dictionary to store benchmark results
custom_results = {'Insertion Sort': []}

# Run benchmarks for each sorting algorithm and array size
for custom_size in custom_sizes:
    custom_array = generate_custom_array(custom_size)

    # Custom Insertion Sort
    custom_ins_time = custom_benchmark('insertion_sort', custom_array)
    custom_results['Insertion Sort'].append(custom_ins_time)
    print(f"Input Size: {custom_size}, Execution Time: {custom_ins_time:.6f} seconds")
# Plotting the results
plt.plot(custom_sizes, custom_results['Insertion Sort'], color='purple')
plt.xlabel('Input Size of Array')
plt.ylabel('Runtime (sec)')
plt.title('Insertion Sort Algorithm')
plt.show()