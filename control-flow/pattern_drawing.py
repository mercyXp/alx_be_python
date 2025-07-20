length = int(input("Enter the size of the pattern:"))

counter = 1
while length > 0:
    for counter in range(counter, length + 1):
        print("*" , end= "")
    print()
    counter += 1
    break