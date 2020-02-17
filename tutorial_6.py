# Python Object Oriented Programming


class Employee(object):
    def __init__(self, first, last):
        self.first = first
        # self.fname = first
        self.last = last
        # self.email = first + "." + last + "@company.com"

    @property
    def email(self):
        # The property decorator helps to define the email method but it can be accessed just like an attribute
        # instead of emp_1.email(), we use emp_1.email directly
        return "{}.{}@company.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    # has to be same name as the method targetted
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    # has to be same name as the method targetted
    def fullname(self):
        print("Delete name")
        self.first = None
        self.last = None


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Steve", "Doe")

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
print()
"""
John
John.Smith@company.com
John Smith
"""

emp_1.first = "Jim"
print(emp_1.first)
print(emp_1.email)
# fullname can now be accessed as an attribute as oppose to previous tutorials where it was a class method
print(emp_1.fullname)
print()
"""
Jim
John.Smith@company.com
Jim Smith
"""

emp_2.fullname = "Jane Doe"
print(emp_2.first)
print(emp_2.email)
print(emp_2.fullname)
print()

del emp_1.fullname
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
print()
