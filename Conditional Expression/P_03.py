p1 = "Make a lot of money "
p2 = "buy now "
p3 = "subscrib this "
p4 = "click this "

message = input("Enter any comment :")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 or message)):
    print ("This comment is spam :")
else:
    print("This comment is not spam")
    