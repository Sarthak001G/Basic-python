x = -5
if x < 0:
    raise ValueError("x cannot be negative")
class CustomError(Exception):
    """A custom exception class"""
    pass

try:
    raise CustomError("This is a custom exception")
except CustomError as e:
    print(f"Caught an error: {e}")
