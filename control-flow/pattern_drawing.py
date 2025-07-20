integer = int(input("Enter the size of the pattern: "))
i = 0

while i < integer:
    for j in range(integer):
        print("*", end="")
    print()
    i += 1