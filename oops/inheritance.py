class employee:
    company ="itc"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


class Programmer(employee):
    company = "itc infotech"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")


    def showlanguage(self):
        print(f"the name is {self.name} amd the salary is {self.language} language")




a = employee()
b = Programmer()

print(a.company,b.company)