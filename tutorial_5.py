class Employee(object):

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # dunder init is init surrounded by double underscores
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        # repr is an unambiguous representation of an object
        # should be used for debugging and logging
        # meant to be seen by other developers
        # dispay something that can be copied and paste to the python interpreter
        # try to return a string that can be used to recreate an object
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        # str is more readable representation of an object
        # meant to used as display to the end user
        return "{} - {}".format(self.fullname(), self.email)

    # method to add 2 employees together to get a result of combined salaries
    def __add__(self, other):
        return self.pay + other.pay

    # method to get the length of an employee's fullname
    def __len__(self):
        return len(self.fullname())


emp_1 = Employee("John", "Doe", 50000)
emp_2 = Employee("Steve", "Smith", 60000)
emp_3 = Employee("Jane", "Doe", 90000)

print(emp_1)
# Output for print(emp_1) without repr method: <__main__.Employee object at 0x03F78070>
# Output for print(emp_1) with repr method: Employee('John', 'Doe', '50000')
# Output for print(emp_1) with str method: John Doe - John.Doe@company.com
print()

# To access the magic/dunder methods directly
print(repr(emp_2))
print(str(emp_2))
print()

print(emp_3.__repr__())
print(emp_3.__str__())
print()

# More dunder methods
print(1 + 2)
print(int.__add__(1, 2))
print("a" + "b")
print(str.__add__("a", "b"))
print()

# add 2 employee objects together to obtain the sum of their salaries
print(emp_1 + emp_2)
print()

print(len("test"))
print("test".__len__())
print()

# use len to return total characters of an employee's fullname
print("Fullname: {}, Length: {}".format(emp_1.fullname(), len(emp_1)))
