class Employee:
    language = "py"#this is class attribute
    salary=120000
    def __init__(self,name,language,salary):
        self.name =name
        self.language=language
        self.salary=salary
        pass


harry=Employee("sarthak","java",12)

#harry.name="Sarthak"#this is object attribute
print(harry.name,harry.language,harry.salary) 