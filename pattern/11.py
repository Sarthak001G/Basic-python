n=5
for i in range (1,n):
    for j in range(1,i+1):
        print(j,end="")

    for k in range(1,n-1):
        print(" "*(2*(n-i)-2),end="")

    for s in range(i,0,-1):
        print(s,end="")
    print()
