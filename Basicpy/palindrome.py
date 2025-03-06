str=input("enter any input")
length=len(str)
mid=length//2
rev=-1
for a in range(mid):
    if str[a]==str[rev]:
        a+=1
        rev-=1
    else:
        print(str,"is not apalindrome")
        break
else:
    print(str,"is a palindrome")