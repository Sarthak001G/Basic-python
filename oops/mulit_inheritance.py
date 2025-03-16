class employee:
    company ="itc"
    name ="default name"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")


class coder:
    language = "Python"
    def printlanguage(self):
        print(f"Out of all language here is ur language{self.language}")

class Programmer(employee,coder):
   # company = "itc infotech"
    

    def showlanguage(self):
        print(f"The name is {self.company} and the language is {self.language} language")




a = employee()
b = Programmer()

b.show()
b.printlanguage()
b.showlanguage()

print(a.company,b.company)