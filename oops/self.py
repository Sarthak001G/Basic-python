class Employee:
    language = "py"#this is class attribute
    salary=120000
    def getinfo(self):
        print(f"{self.language}  {self.salary}")
    @staticmethod
    def greet():
        print("hello sir")


harry=Employee()
harry.name="Sarthak"#this is object attribute
print(harry.name,harry.language,harry.salary) 
harry.getinfo()
harry.greet()
#Employee.greet(harry)