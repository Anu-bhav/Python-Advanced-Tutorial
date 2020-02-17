# Python Object Oriented Programming


class Employee(object):
    def __init__(self, first, last, pay):
        self.first = first
        # self.fname = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        # The instance is always passed as an argument automatically
        # to handle the argument always put self as the first argument
        return "{} {}".format(self.first, self.last)


emp_1 = Employee("Test", "User", 50000)
emp_2 = Employee("Test2", "User2", 60000)

print(emp_1)
print(emp_2)
print()

# emp_1.first = "Test"
# emp_1.last = "User"
# emp_1.email = "Test.User@example.org"
# emp_1.pay = 50000

# emp_2.first = "Test2"
# emp_2.last = "User2"
# emp_2.email = "Test2.User2@example.org"
# emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)
print()

# print("{} {}".format(emp_1.first, emp_1.last))

# Invoking the method from the instance
# Employee.fullname(emp_1) - this happens in background
print(emp_1.fullname())

# Invoking the method using the class name directly and passing the instance as argument
print(Employee.fullname(emp_1))
