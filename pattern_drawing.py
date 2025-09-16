size = int(input("enter the number : "))
current_row = 0
while current_row < size:
    for column in range(size):
        print("*",end="")
    print()
    current_row += 1