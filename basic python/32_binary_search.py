# Search for a number in a sorted list using binary search

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


numbers = [3, 8, 15, 23, 42, 56, 71, 89]
print("List:", numbers)
print("Index of 42:", binary_search(numbers, 42))
print("Index of 50:", binary_search(numbers, 50))
