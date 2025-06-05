size = int(input("Enter the size of the pattern: "))
count = 1
while count <= size:
    for i in range(1, size+1):
        print("*", end="")
    print()
    count += 1
