matrix = []

row = int(input("Enter Number Of Rows :-"))
column = int(input("Enter Number Of Column :-"))

for ro in range(1, row+1):
    matrix.append([])
    for col in range(1, column+1):
        item = int(input(f"Enter Numbers Of {ro}th Row :-"))
        matrix[ro-1].append(item)

for i in range(1,row+1):
    aug_item = int(input("Enter Augmented item :-"))
    matrix.append([aug_item])
        
print(matrix)

for main_i in range(len(matrix[0])):
    
    pivot_row = int(input("Enter Pivot Row :-"))
    pivot_column = int(input("Enter Pivot Column :-"))
    length = len(matrix[pivot_row-1])

    j=0

    pivot = matrix[pivot_row-1][pivot_column-1]
    matrix[pivot_row+(row-1)][0] = matrix[pivot_row+(row-1)][0]/pivot 
    for i in matrix[pivot_row-1]:
        change = i/pivot
        matrix[pivot_row-1][j] = change
        j += 1

    for item1 in matrix:
        if len(item1) == len(matrix[pivot_row-1]):
            if item1 != matrix[pivot_row-1]:
                multiply = item1[pivot_column-1]
                for i in range(len(matrix[pivot_row-1])):
                    item1[i] = item1[i] - matrix[pivot_row-1][i]*multiply 
                matrix[matrix.index(item1)+(row)][0] =  matrix[matrix.index(item1)+(row)][0] - matrix[pivot_row+(row-1)][0]*multiply
    print(matrix) 