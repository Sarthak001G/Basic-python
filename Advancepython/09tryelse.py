try:
    # Code that might raise an exception
    num = int(input("Enter a number: "))
    result = 100 / num  # May raise ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
else:
    # This runs only if no exception occurs
    print(f"Division successful, result: {result}")
