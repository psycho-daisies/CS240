# Merge Sort Assignment
# By: Troy Brunette

"""Uses Binary Search from past assignment and a couple functions for reading the provided numbers text file"""
from res.binarysearch import binary_search
from res.importfile import read_file, print_sorted

# Merge Sort recursively divides the array into sub-arrays and merges it back in sorted order
def merge_sort(arr):
    if len(arr) <= 1:  # BASE CASE
        return arr

    # Divide & Conquer: split the array into two sub-arrays: left & right
    mid = len(arr) // 2
    left = arr[:mid]  # from start of array to the middle
    right = arr[mid:]  # from the middle to the end

    # RECURSIVE CASE: recursively splits each sub-array in half
    merge_sort(left)
    merge_sort(right)

    # Sorts and then merges the sub-arrays
    return merge(arr, left, right)

# Merge compares the elements in the sub-arrays and puts them back together in order
def merge(arr, left, right):
    i = j = k = 0

    # Compares the sub-arrays and puts them in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Merges the sub-arrays
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    # Copy the remaining elements
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


# Testing Merge Sort on a small array
numbers = [2, 9, 6, 3, 7, 5, 8, 4, 1]
print(merge_sort(numbers))

# Testing Merge Sort on provided numbers text file
# Searching for specified numbers using Binary Search
unsorted = read_file("res/numbers-4.txt")
merge_sort(unsorted)
print_sorted(unsorted)
target = 11559
target2 = 90262
index, count = binary_search(unsorted, target)
index2, count2 = binary_search(unsorted, target2)
print(f"Target: {target} at Index: {index}")
print(f"Target: {target2} at Index: {index2}")
