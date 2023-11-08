
rows = 6
num = 1

# Outer loop for the rows
for i in range(1, rows + 1):
    # Print spaces for alignment
    print(' ' * (rows - i), end='')

    # Inner loop for printing numbers
    for j in range(1, i + 1):
        print(num, end=' ')
        num += 1

    # Move to the next line after each row is printed
    print()