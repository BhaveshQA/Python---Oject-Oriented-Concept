"""
composition : delegate some responsibility of one class to other class
-Here we not use any inheritance
-Here one class act as container and one class act content
- Here we create instace of one class into other's class init method
- so if we delete one object it automatically delete the other class object
- Ex. Salary class is 'part of' Employee class
"""

class Employee:

    def __init__(self,name,age,pay,bonus):
        self.name = name
        self.age = age

        # here create object of the other class

        self.salary_object = Salary(pay,bonus)

    def total_salary(self):
        return self.salary_object.salary_cal()



class Salary:

    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus

    def salary_cal(self):

        return  self.pay *12 + self.bonus




# create Employee class object
emp =Employee("Bhavesh", 31, 50000,10000)
print(emp.total_salary())