class Employee(object):

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, programming_language):
        # super().__init__() will pass the same parameters to the parent class __init__ function
        super().__init__(first, last, pay)
        # the parent class name can also be used
        # Employee.__init__(self, first, last, pay)

        self.programming_language = programming_language


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        # Never pass mutable data type like list or dictionnary as an argument
        super().__init__(first, last, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("--> ", emp.fullname())


dev_1 = Employee("John", "Doe", 50000)
dev_2 = Developer("Steve", "Smith", 60000, "Python")
dev_3 = Developer("Jane", "Doe", 90000, "Java")

# Even without any customisation to the Developer class, it inherits all the methods and attributes from its parent class
print(dev_1.email)
print(dev_2.email)
print()

# print(help(Developer))
# print()

print("Employee Class")
print("{} : {}".format(dev_1.fullname(), dev_1.pay))
dev_1.apply_raise()
print("{} : {}".format(dev_1.fullname(), dev_1.pay))
print()

print("Developer Class")
print("{} : {}".format(dev_2.fullname(), dev_2.pay))
dev_2.apply_raise()
print("{} : {}".format(dev_2.fullname(), dev_2.pay))
print()

print("Inheritance")
print("{} : {} : {}".format(dev_2.fullname(), dev_2.pay, dev_2.programming_language))
print("{} : {} : {}".format(dev_3.fullname(), dev_3.pay, dev_3.programming_language))
print()

print("Manager Class")
mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])
print(mgr_1.email)
mgr_1.print_emp()
print()

mgr_1.add_emp(dev_2)
mgr_1.add_emp(dev_3)
mgr_1.print_emp()
print()

mgr_1.remove_emp(dev_1)
mgr_1.print_emp()
print()

print("Check if an object is an instance of a class")
print("if mgr_1 is an instance of class Manager: ", isinstance(mgr_1, Manager))
print("if mgr_1 is an instance of class Employee: ", isinstance(mgr_1, Employee))
print("if mgr_1 is an instance of class Developer: ", isinstance(mgr_1, Developer))
print()

print("Check if a class is a subclass of an another class")
print("Is Developer a subclass of Employee: ", issubclass(Developer, Employee))
print("Is Manager a subclass of Employee: ", issubclass(Manager, Employee))
print("Is Developer a subclass of Manager: ", issubclass(Developer, Manager))
