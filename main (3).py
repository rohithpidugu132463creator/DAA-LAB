import time

# Merge Sort Function
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        # Recursively sort both halves
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merge the two halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements of left half
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy remaining elements of right half
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# User input
n = int(input("Enter the number of elements: "))

arr = []
print(f"Enter {n} elements:")
for i in range(n):
    arr.append(int(input()))

# Start timer
start_time = time.time()

# Perform Merge Sort
merge_sort(arr)

# Stop timer
end_time = time.time()

# Calculate execution time
execution_time = end_time - start_time

# Display sorted array
print("\nSorted Array:")
print(arr)

# Display execution time
print(f"\nExecution Time: {execution_time:.6f} seconds")

# Display time complexity
print("\nTime Complexity:")
print("Best Case    : O(n log n)")
print("Average Case : O(n log n)")
print("Worst Case   : O(n log n)")
print("Space Complexity: O(n)")

# 1.2
import time
import random

# Partition function
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Quick Sort function
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Generate a random list
n = 10  # Number of elements in the random list
arr = [random.randint(0, 100) for _ in range(n)] # Generate random integers between 0 and 100

print("Original Array:")
print(arr)

# Start timer
start_time = time.time()

# Perform Quick Sort
quick_sort(arr, 0, n - 1)

# Stop timer
end_time = time.time()

# Calculate execution time
execution_time = end_time - start_time

# Display sorted array
print("\nSorted Array:")
print(arr)

# Display execution time
print(f"\nExecution Time: {execution_time:.6f} seconds")

# Display time complexity
print("\nTime Complexity:")
print("Best Case    : O(n log n)")
print("Average Case : O(n log n)")
print("Worst Case   : O(n^2)")
print("Space Complexity: O(log n)")


#1.3
import time
# Input from the user
n = int(input("Enter the number of elements: "))
arr = []
print(f"Enter {n} elements:")
for i in range(n):
    arr.append(int(input()))

# Start timer
start_time = time.time()

# Bubble Sort
for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Stop timer
end_time = time.time()

# Calculate execution time
execution_time = end_time - start_time

# Display sorted array
print("\nSorted Array:")
print(arr)

# Display execution time
print(f"\nExecution Time: {execution_time:.6f} seconds")

# Display time complexity
print("\nTime Complexity:")
print("Best Case    : O(n^2)")
print("Average Case : O(n^2)")
print("Worst Case   : O(n^2)")
print("Space Complexity: O(1)")

#1.4
import time

# Input from the user
n = int(input("Enter the number of elements: "))

arr = []
print(f"Enter {n} elements:")
for i in range(n):
    arr.append(int(input()))

# Start timer
start_time = time.time()

# Selection Sort
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    # Swap the minimum element with the current element
    arr[i], arr[min_index] = arr[min_index], arr[i]

# Stop timer
end_time = time.time()

# Calculate execution time
execution_time = end_time - start_time

# Display sorted array
print("\nSorted Array:")
print(arr)

# Display execution time
print(f"\nExecution Time: {execution_time:.6f} seconds")

# Display time complexity
print("\nTime Complexity:")
print("Best Case    : O(n^2)")
print("Average Case : O(n^2)")
print("Worst Case   : O(n^2)")
print("Space Complexity: O(1)")

#1.5
import time

# Input from the user
n = int(input("Enter the number of elements: "))

arr = []
print(f"Enter {n} elements:")
for i in range(n):
    arr.append(int(input()))

# Start timer
start_time = time.time()

# Insertion Sort
for i in range(1, n):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

# Stop timer
end_time = time.time()

# Calculate execution time
execution_time = end_time - start_time

# Display sorted array
print("\nSorted Array:")
print(arr)

# Display execution time
print(f"\nExecution Time: {execution_time:.6f} seconds")

# Display time complexity
print("\nTime Complexity:")
print("Best Case    : O(n)")
print("Average Case : O(n^2)")
print("Worst Case   : O(n^2)")
print("Space Complexity: O(1)")


