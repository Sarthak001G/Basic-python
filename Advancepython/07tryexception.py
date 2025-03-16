try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except TypeError:
    print("Error: Type mismatch occurred.")
except Exception as e:  # Catches all other exceptions
    print(f"An unexpected error occurred: {e}")
