class employee:
    def __init__(self):
        print("constructor of employee")
    a=1

class programmer(employee):
    def __init__(self):
        print("constructor of programmer")
    b=2


class Manager(programmer):
    def __init__(self):
        super().__init__()
        print("constructor of manager")
    c=3

o = employee()
print(o.a)#prints a attribute
#print(o.b)#show error as there is no atrribute b

o = programmer()
print(o.a,o.b)

o= Manager()
print(o.a,o.b,o.c)