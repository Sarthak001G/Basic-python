rows = 6

# Upper half of the pattern
for i in range(1, rows + 1):
    print("* " * i)

# Lower half of the pattern
for i in range(rows - 1, 0, -1):
    print("* " * i)
