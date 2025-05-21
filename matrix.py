matrix=[]
for i in range(3):
    row=[]
    for j in range(3):
        val=int(input(f"Enter the values {i},{j}:"))
        row.append(val)

    matrix.append(row)
    for row in matrix:
        print(row)