# Quicksort Assignment
# By: Troy Brunette
"""I found the CS Dojo YouTube video on Quicksort a great resource to help with this assignment."""

from res.importfile import read_file, print_sorted
from res.binarysearch import binary_search


def quicksort(arr, l, r):
    if l >= r:  # BASE CASE
        return
    # Recursive CASE: partition / choosing a pivot
    p = partition(arr, l, r)

    # calling quicksort on the two groups
    quicksort(arr, l, p - 1)
    quicksort(arr, p + 1, r)

    return arr


# Separates numbers into two groups
# Numbers less than the pivot
# Numbers greater than the pivot
def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] <= pivot:
            i = i + 1

            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i + 1], arr[r]) = (arr[r], arr[i + 1])

    return i + 1


# Testing Quicksort on a small array
numbers = [2, 9, 6, 3, 7, 5, 8, 4, 1]
print(quicksort(numbers, 0, len(numbers) - 1))

# Testing Quicksort on provided numbers text file
# Searching for specified numbers using Binary Search
unsorted = read_file("res/numbers-4.txt")
print_sorted(unsorted)
sorted = quicksort(unsorted, 0, len(unsorted) - 1)
target = 11559
target2 = 90262
index, iters = binary_search(sorted, target)
index2, iters2 = binary_search(sorted, target2)
print(f"Target: {target} at Index: {index}")
print(f"Target: {target2} at Index: {index2}")
# print(unsorted[index])

"""
6. Use the uploaded file to verify your sort algorithms are working. numbers-4.txt
Download numbers-4.txt  What is the position of 90262? What is the position of 11559? 

The position of 90262 is index 3608 / line 3609.
The number 11559 is not in the list of numbers.

"""
