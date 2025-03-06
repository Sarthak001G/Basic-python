class calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"the sq of num is {self.n*self.n}")


a=calculator(45)
a.square()