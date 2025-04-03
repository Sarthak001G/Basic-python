def print_burfi(n):
    # Upper part of the diamond
    for i in range(1, n+1):
        print(' ' * (n-i) + '*' * (2*i-1))

    # Lower part of the diamond
    for i in range(n-1, 0, -1):
        print(' ' * (n-i) + '*' * (2*i-1))

# Call the function
print_burfi(5)
