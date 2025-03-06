class calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"the sq of num is {self.n*self.n}")

    @staticmethod
    def hello():
        print("Hello world")



a=calculator(45)
a.hello()
a.square()