class Employee:
    company = 'New Tutorial Gateway'

    def __init__(self, name, age, gender):
        self.name = name
        self.gender = gender
        self.age = age
        

    def func_message(self):
        print(self.name + ' is learning Python Programming')


emp1 = Employee('Roy Anderson', 'Male', 25)
print(emp1.company)
print(emp1.name)  # Mike
print(emp1.gender)
print(emp1.age)  # 25
emp1.func_message()

print("Print another example")

emp1 = Employee('Amal bandara', 'Male', 20)
print(emp1.company)
print(emp1.name)  # Mike
print(emp1.gender)
print(emp1.age)  # 25
emp1.func_message()
