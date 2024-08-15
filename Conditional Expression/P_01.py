a1 = int(input('Enter any Number:'))
a2 = int(input('Enter any Number:'))
a3 = int(input('Enter any Number:'))
a4 = int(input('Enter any Number:'))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is a1 ")
elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is a2 ")
elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is a3 ")
else:
    print("Greatest number is a4 ")