#self show instance attribute
class employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")


    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    

    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]



e = employee()
e.a = 45

e.name = "harry"

e.show()
"""The @classmethod is a decorator in Python that is used to define a method inside a class that is bound to the class rather than an instance of the class. This means that the method can be called on the class itself, rather than needing an instance (object) of the class.

A classmethod takes at least one argument, which is typically called cls, representing the class itself. This allows the method to modify class-level attributes or call other class methods."""