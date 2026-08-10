import time

# Linear Search Function
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


# Binary Search Function
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Main Program
n = 100000
arr = list(range(1, n + 1))  # Creating a sorted array

key = int(input("Enter element to search: "))

# Linear Search Timing
start = time.perf_counter()
index = linear_search(arr, key)
stop = time.perf_counter()

print("\nLinear Search")
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")

print("Time Taken:", (stop - start) * 1_000_000, "microseconds")

# Binary Search Timing
start = time.perf_counter()
index = binary_search(arr, key)
stop = time.perf_counter()

print("\nBinary Search")
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")

print("Time Taken:", (stop - start) * 1_000_000, "microseconds")