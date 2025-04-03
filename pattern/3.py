def pattern(n):
    for i in range (n):
        
        for j in range (i+1):
            print("*",end="")
        print()
    for i in range (n):
        
        for j in range (n-i):
            print("*",end="")

    
        print()




        
n=int(input("enter any num"))
s=pattern(n)
