"""Reads the numbers text file and prints to a new text file"""


def read_file(filename):
    arr1 = []
    # Open the file in read mode
    file = open(filename, "r")
    line = file.readline()
    # Read each line in the file
    while line:
        # Append each line to the array
        arr1.append(int(line.strip()))
        line = file.readline()
    file.close()
    return arr1


def print_sorted(arr):
    # Open a file for writing ('w' mode)
    with open('sorted_numbers-4.txt', 'w') as file:
        # Write content to the file
        for i in range(len(arr)):
            file.write(str(arr[i]) + "\n")
        file.close()
        
