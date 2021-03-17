class Employee:

    raise_amount= 1.04 

    # apply_raise is a class variable .

    # it can be accessed from the instance also . but the instance will first
    # find it from the class itself .


    no_of_emps = 0

    # getting the number of employeees . 
    # increment it as a new instance is created , so that can be done by
    # incrementing it in __init__ method .


    def __init__(self, first , last , pay):
        self.first = first 
        self.last = last 
        self.pay = pay

        Employee.no_of_emps += 1
    # the init method is called each and every time an instance is created.

    # the instance have the attributes as first , last , pay . these are the properties 
    # of the instance and are known as attributes of the instance .

    def full_name(self):
        return "{} {} ".format(self.first , self.last)

    def apply_raise(self):
        self.pay = self.pay* self.raise_amount
     #  self.pay = self.pay * Employee.rasie_amount  

        # if the apply_raise function wrote self.pay * raise_amonut
        # the NameError would appear saying raise_amount is not defined

        # apply_raise  can be accessed from the instance also .
        #  but the instance will first find it from the class itself .

        # and apply_raise is not an instance variable .

        # see the output below .

emp_1 = Employee("Om" , "Kashyap" , 100000)
emp_2 = Employee("Nabi","Baksh"   , 10)

print(emp_1.raise_amount)
print(Employee.raise_amount)
print("\n\n")
print(emp_1.pay) 
emp_1.apply_raise()
print(emp_1.pay)
print("\n\n")
print(emp_1.__dict__,"\n\n\n") # no raise_amount in emp_1
# raise_amount is not a instance variable .
print(Employee.__dict__)


# but you can individualy set the apply_raise to be the instance variable
print("\n\n")
emp_1.raise_amount = 1.1
# the above program creates a new atttribute  for emp_1 ,
# the raise_amount in the class changes to 1.1 
print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_2.raise_amount)
print("\n\n")
print(emp_1.__dict__) # the dict would include raise_amount
print("\n\n")
emp_1.apply_raise() 
print(emp_1.pay)
print(emp_2.pay)
print("\n\n")
print(Employee.no_of_emps)