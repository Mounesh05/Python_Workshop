matrix = []
n = int(input("Enter number of rows: "))
for i in range(n):
    row = []
    for j in range(n):
        val = int(input(f"Enter the value at position ({i},{j}): "))
        row.append(val)
    matrix.append(row)
print("\nMatrix:")
for row in matrix:
    print(row)
primary_diagonal_sum = sum(matrix[i][i] for i in range(n))
secondary_diagonal_sum = sum(matrix[i][n - i - 1] for i in range(n))
if n % 2 == 1:
    center = matrix[n // 2][n // 2]
    total_diagonal_sum = primary_diagonal_sum + secondary_diagonal_sum - center
else:
    total_diagonal_sum = primary_diagonal_sum + secondary_diagonal_sum
print(f"\nSum of Primary Diagonal Elements: {primary_diagonal_sum}")
print(f"Sum of Secondary Diagonal Elements: {secondary_diagonal_sum}")
print(f"Total Sum of Diagonal Elements: {total_diagonal_sum}")
