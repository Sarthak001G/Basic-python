# Defining a class named 'Demo'
class Demo:
    a = 4  # 'a' is a class variable (shared by all objects of this class)

# Creating an object 'o' of the Demo class
o = Demo()

# Accessing and printing the class variable 'a' using the object
print(o.a)  # Output: 4 (Initially, 'a' is taken from the class variable)

# Assigning a new value to 'a' through the object 'o'
o.a = 0  # This creates a new instance variable 'a' for object 'o', without modifying the class variable

# Printing the value of 'a' for object 'o'
print(o.a)  # Output: 0 (Instance variable 'a' is now 0 for object 'o')

# Printing the class variable 'a' using the class name
print(Demo.a)  # Output: 4 (Class variable remains unchanged)
