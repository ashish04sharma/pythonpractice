# Add two matrices using nested lists

a = [[1, 2, 3],
     [4, 5, 6]]
b = [[7, 8, 9],
     [1, 2, 3]]

result = []
for i in range(len(a)):
    row = []
    for j in range(len(a[0])):
        row.append(a[i][j] + b[i][j])
    result.append(row)

print("Sum of matrices:")
for row in result:
    print(row)
