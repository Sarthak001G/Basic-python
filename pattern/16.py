n = 5  # Number of rows

for i in range(n, -1, -1):
    for j in range(0, i+1):
        print(chr(65+j), end="")
    print()
