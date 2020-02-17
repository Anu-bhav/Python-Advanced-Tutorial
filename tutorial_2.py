class Employee(object):

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        # Here the class name is used instead of self so that noone can overwrite the value of num_of_emps
        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(self.pay * raise_amount) - errors out as it cannot be accessed directly

        # Employee.raise_amount does not give the ability to an instance to change its value
        # self.pay = int(self.pay * Employee.raise_amount)

        # self.raise_amount gives the ability to an instance to change its value
        self.pay = int(self.pay * self.raise_amount)
        # When using self, it allows any subclass to change its value


emp_1 = Employee("Test", "User", 50000)
emp_2 = Employee("Test2", "User2", 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print()

print(Employee.raise_amount)
# The instances don't have the attributes themselves
# They are accessing their parent class raise_amount attribute
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print()

# This prints out the namespace of instance emp_1
print(emp_1.__dict__)
# This prints out the namespace of the class Employee
print(Employee.__dict__)  # raise_amount can be accessed from here
print()

# Changing the value of raise_amount for the Employee class
Employee.raise_amount = 1.05
print(Employee.raise_amount)
# The instances don't have the attributes themselves
# They are accessing their parent class raise_amount attribute
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print()

# Changing the value of raise_amount for the emp_1 instance
emp_1.raise_amount = 1.06
print(Employee.raise_amount)
# The instances don't have the attributes themselves
# They are accessing their parent class raise_amount attribute
print(emp_1.raise_amount)
print(emp_1.__dict__)  # emp_1 now has raise_amount within it's namespace
print(emp_2.raise_amount)
print()

# this class global variable cannot be modified by any instance
print(Employee.num_of_emps)
