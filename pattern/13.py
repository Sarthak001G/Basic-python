def pattern(n):
    p=0
    for i in range (n):
        for j in range (i+1):
            
            print(chr(65+p),end=" ")
            p+=1
        print()

n=int(input("enter any num"))
s=pattern(n)