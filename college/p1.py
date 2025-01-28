import keyword
L1 =['4','5','if','else','for',"For"]
Keyword = keyword.kwlist
for i in range(0,6):
    if L1 in Keyword:
        print(L1[i],"is  a keyword")
    else :
        print(L1[i],"is not a keyword")