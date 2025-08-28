class Employee:
    def __init__(self, name):
        self.name = name
    def __init__(self, roles):
        self.roles = roles
    def __init__(self, department):
        self.department = department
    def __init__(self, salary):
        self.salary = salary
emp1 =("QASIM","Software Engineer","IT",60000)
emp2 =("ADNAN","Data Scientist","Analytics",70000)
emp3 =("ZUBAIR","Product Manager","Product",80000)
print(emp1)
print(emp2)
print(emp3)
class ENGG(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineering","IT", "40")
emp1 = ENGG("kaif", 25)
print(emp1.name)
print(emp1.age)
    
emp