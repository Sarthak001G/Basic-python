try:
    # Code that may raise an exception
    num = int(input("Enter a number: "))
    result = 10 / num  # Might raise ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
finally:
    # This block ALWAYS runs, whether an exception occurs or not
    print("Execution complete. Cleaning up resources if necessary.")





def divide_with_finally():
    try:
        num = int(input("Enter a number: "))
        result = 10 / num  # Might raise ZeroDivisionError
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
    finally:
        print("Execution complete. Cleaning up resources if necessary.")

# Calling the function
divide_with_finally()





def divide_with_finally():
    try:
        num = int(input("Enter a number: "))
        result = 10 / num  # Might raise ZeroDivisionError
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
    
    print("Execution complete. Cleaning up resources if necessary.")

# Calling the function
divide_with_finally()
