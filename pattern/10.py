n = 5  # Number of rows

for i in range(1, n + 1):
    for j in range(i):
        print((i + j) % 2, end=" ")
    print()
