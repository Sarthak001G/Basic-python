# Importing randint function from the random module
from random import randint

# Defining a class 'tran' (should be 'Train' for better readability)
class tran:
    
    # Constructor to initialize the train number
    def __init__(self, Train_no):
        self.Train_no = Train_no  # Instance variable to store train number

    # Method to book a train ticket
    def booked(harry, fro, to):
        print(f"Train {harry.Train_no} booked from {fro} to {to}.")

    # Method to get the train status
    def getstatus(self):
        print(f"Train no {self.Train_no} is on time.")

    # Method to calculate and print the fare
    def getfare(self, fro, to):
        fare = randint(222, 555)  # Generating a random fare
        print(f"Fare for train no {self.Train_no} from {fro} to {to} is ₹{fare}.")

# Creating an object 't' of class 'tran' with train number 123456
t = tran(123456)

# Calling methods on the object
t.booked("Rampur", "Delhi")   # Output: Train 123456 booked from Rampur to Delhi.
t.getfare("Rampur", "Delhi")  # Output: Fare for train no 123456 from Rampur to Delhi is ₹<random number>.
t.getstatus()                 # Output: Train no 123456 is on time.
