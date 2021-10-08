class Employee:
    company = 'New Tutorial Gateway'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def func_message(self):
        print(self.name + ' is learning Python Programming')


emp1 = Employee('Roy Anderson', 25, 'Male')
print(emp1.company)
print(emp1.name)  # Mike
print(emp1.age)  # 25
print(emp1.gender)
emp1.func_message()
