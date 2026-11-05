# Find the second largest number in a list without sorting

def second_largest(numbers):
    largest = None
    second = None
    for num in numbers:
        if largest is None or num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num
    return second


values = [12, 45, 7, 45, 33, 21]
print("List:", values)
print("Second largest:", second_largest(values))
