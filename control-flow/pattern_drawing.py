
size = int(input("Enter the size of the pattern: "))

row = 0

while row < size:
    # Use a for loop to print asterisks for the current row
    for i in range(size):
        print("*", end="")
    # Move to the next line after completing the row
    print()
    # Increment row counter
    row += 1