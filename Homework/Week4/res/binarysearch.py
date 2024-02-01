"""From the Binary Search assignment"""
# Binary Search Assignment 1
# By: Troy Brunette


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
