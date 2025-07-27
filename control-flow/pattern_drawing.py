size= int(input("Enter the size of the pattern: "))
row = 0
while row < size:
    for column in range(size):
        print("*", end="") # Print asterisk without a newline
    print() # Move to the next line after each row
    row += 1