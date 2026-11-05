# Sort a list using selection sort

def selection_sort(arr):
    for i in range(len(arr) - 1):
        smallest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
    return arr


numbers = [29, 10, 14, 37, 13]
print("Original list:", numbers)
print("Sorted list:", selection_sort(numbers.copy()))
