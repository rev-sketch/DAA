'''Problem 2 :Remove Duplicates from array'''

def remove_duplicates(array):
    if len(array) == 0:
        return [] 
    result = [array[0]] 
    for i in range(1, len(array)): 
        if array[i] != array[i - 1]: 
            result.append(array[i]) 
    return result


input_string = input("Enter the elements of the array separated by spaces: ")
input_array = list(map(int, input_string.split()))
output_array = remove_duplicates(input_array)
print("Input Array:", input_array)
print("Output Array after removing duplicates:", output_array)
# Example 1
#Enter the elements of the array separated by spaces: 2 2 2 2 2
# Input Array: [2, 2, 2, 2, 2]
# Output Array after removing duplicates: [2]

# Example 2
# Enter the elements of the array separated by spaces: 1 2 2 3 4 4 5 5
# Input Array: [1, 2, 2, 3, 4, 4, 5, 5]
# Output Array after removing duplicates: [1, 2, 3, 4, 5]