class Employee:

    raise_amount = 1.04 

    def __init__(self , first , last , pay):
        self.first = first 
        self.last = last 
        self.pay = pay 
        self.email = "{}.{}@email.com"


    def fullname(self):
        return "{} {}".format(self.first , self.last )

    def __repr__(self):
        return "Employee('{}' , '{}' , {})".format(self.first , self.last , self.pay)

    def __str__(self):
        return "{}  - {} ".format(self.first , self.last)

emp_1 = Employee("Om" , "Kashyap" , 100000)
emp_2 = Employee("Someone" , "Unknown" , 1000)

print(repr(emp_1))
print(emp_1.__repr__())
# the dunder and the funciton repr works the same way .


print("\n\n")

print(str(emp_2))
print(emp_2.__str__())
# here too , the dunders and the function work the same way.
# these are the magic methods .     

print(1+2)
# this adds up integer , because in background , the dunder 
# function backs it . it uses integer dunder.
