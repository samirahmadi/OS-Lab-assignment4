high= int(input("Enter n: "))

for i in range(1, high+1):
    for j in range(1,high-i+1):
        print(" ", end="")

    for j in range(1, 2*i):
        print("*", end="")
    print()

for i in range(high-1,0, -1):
    for j in range(1,high-i+1):
        print(" ", end="")
        
    for j in range(1, 2*i):
        print("*", end="")
    print()