""" Wap to find whether the input digit is 1,2,3"""
num=int(input("Enter the number between 0 to 999 ="))
if num<0 :
    print("Enter the number Greater than 0")
elif num>999:
    print ("enter the number Less than 999")
else:
    if num<10:
        print("Number is 1 digit")
    elif num<100:
        print("Number is 2 digit ")
    else:
        print("Number is 3 digit number")