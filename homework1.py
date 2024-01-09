# Binary Search Assignment 1
# By: Troy Brunette

def readfile(file_name):
    arr1 = []
    # Open the file
    file = open("numbers.txt", "r")
    # Read each line and add to array
    for line in file:
        # Append each line to the array
        arr1.append(line.strip())

    file.close()
    return arr1


def binary_search(lines_array, target_num):
    counter = 0  # Counter for iterations
    low = 0
    high = len(lines_array) - 1

    while low <= high:
        counter += 1  # Iteration count
        mid = (low + high) // 2  # take the middle of the search area
        mid_value = int(lines_array[mid])  # convert to int

        if mid_value == target_num:
            return mid, counter

        elif mid_value < target_num:
            low = mid + 1

        else:
            high = mid - 1

    return -1, counter


arr2 = readfile('numbers.txt')

target = 33874
index, iterations = binary_search(arr2, target)

if index != -1:
    print(f"{target} found at index {index} in {iterations} iterations")

else:
    print(f"Target not found!")
