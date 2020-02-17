import datetime


class Employee(object):

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        # Class method is used as an alternative constructor
        fname, lname, emp_pay = emp_str.split("-")
        return cls(fname, lname, emp_pay)

    @staticmethod
    def is_workday(day):
        # Static method don't pass anything i.e self, cls automatically
        # They behave just like regular functions
        # We only include them in the class because they have some logical function with the class

        if day.weekday() == 5 or day.weekday() == 6:
            # weekday: 0 is monday and 6 is sunday
            return False
        return True


emp_1 = Employee("Test", "User", 50000)
emp_2 = Employee("Test2", "User2", 60000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print()

# Using the class method, means any change to this method will affect any instance associated to it
Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print()

# Using the class method, means any change to this method will affect any instance associated to it
# Even though emp_1 is used for the class method, every other instance of that class has been affected
emp_1.set_raise_amount(1.06)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print()

# Classmethods can be used as alternative constructers, this can provide multiple ways of creating the object
# Consider common use case where a single string, having the first, last and pay are separated by a - needs to be created as an Employee Instance
emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

# Normal logic to tackle the problem
first, last, pay = emp_str_1.split("-")

new_emp_1 = Employee(first, last, pay)
print(new_emp_1.email)
print(new_emp_1.pay)

# from_string alternative constructor can now be used to create new instances of the class
new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.email)
print(new_emp_2.pay)

new_emp_3 = Employee.from_string(emp_str_3)
print(new_emp_3.email)
print(new_emp_3.pay)
print()

test_work_day = datetime.date(2016, 7, 10)  # 10th is a sunday
# is_workday is a static method, it behaves like a regular function and takes only defined parameters
print(Employee.is_workday(test_work_day))

test_work_day = datetime.date(2016, 7, 11)  # 11th is a monday
print(Employee.is_workday(test_work_day))
print()
