def pattern(n):
    for i in range (n):
        
        for j in range (i+1):
            print(j,end="")
        print()
    for i in range (n):
        
        for j in range (n-i):
            print(j, end="")

    
        print()




        
n=int(input("enter any num"))
s=pattern(n)
