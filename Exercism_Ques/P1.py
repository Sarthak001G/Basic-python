"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# Define constants
EXPECTED_BAKE_TIME = 40  # Time lasagna needs to bake in the oven
PREPARATION_TIME = 2     # Preparation time per layer in minutes

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time based on the number of layers.

    :param number_of_layers: int - the number of lasagna layers being prepared.
    :return: int - preparation time (in minutes).

    Function that calculates the total preparation time for the lasagna 
    based on a constant time per layer.
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time.

    :param number_of_layers: int - the number of lasagna layers.
    :param elapsed_bake_time: int - time the lasagna has spent baking.
    :return: int - total elapsed time (in minutes).

    Function that calculates the total time spent on lasagna preparation
    and baking.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

# Example Usage
if __name__ == "__main__":
    print(bake_time_remaining(20))  # Should output 20
    print(preparation_time_in_minutes(3))  # Should output 6
    print(elapsed_time_in_minutes(3, 20))  # Should output 26
