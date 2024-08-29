n = int(input("Enter any number"))

for i in range(2,n):
    if(n%i)==0:
        print("number is not prime")
        break
else:
     print("Number is prime")