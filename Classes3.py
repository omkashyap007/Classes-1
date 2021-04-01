class Employee:

    raise_amount = 1.04

    def __init__(self , first , last , pay ) :
        self.first = first 
        self.last = last 
        self.pay = pay 

    def full_name(self) :
        return "{} {} ".format(self.first , self.last ) 

    def apply_raise(self) -> int:
        self.pay = int(Employee.raise_amount * self.pay)

    # these (full_name , apply_raise) are the regular methods
    # and these methods take instances as default varivbles .
    # the common convention for the instance in the phthon is self .

    # @classmethod take the defualt variavble as class .
    # the common name,convention for the class is cls.

    @classmethod 
    def set_raise_amount(cls , amount) :
        cls.raise_amount = amount 

    # the class method take the class as default varaible and
    # this can be used to alter the values defined in the 
    # class . like the raise_amount .


    # the @classmethods can be used as alternative constructors .
    # these can be used to create the instances 

    @classmethod 
    def from_string(cls , string ) :
        first , last , pay = string.split("-")
        return cls(first , last , pay)

    # string  = "Someone-Unknown-101010"
    # from_string(string)
    # and done .

    # now about the statcic methods .

    # the @classmethods take class as variable as cls and ,
    # the regular methods take instance as the default variable as self
    
    # the @staticmethods take nothing as default variable .
    # savage as F 😎😎😎
    # they dont take anything as varible .

    # these methods are similar to regular functions and as they dont 
    # parse any arguments , they are used to fetch some details ,
    # or create funcitons which have some interconnection between 
    # the funciton . 

    # checking that the day is workday or not . 

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6 :
            return False
        return True



emp_1 = Employee("Om"  , "Kashyap" , 100000)
emp_2 = Employee("Nabi" , "Baksh " , 1000)

print(emp_1.raise_amount)
print(Employee.raise_amount)

# the emp_1 and the Employee.raise_amount is the same because 
# the emp_1 retrives the raise_amount from the Employee class .



print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

Employee.set_raise_amount(1.12)

emp_1.apply_raise()
print(emp_1.raise_amount)
print(emp_1.pay)


# using the @classmethod as alternatvie constructor . 
# call it from the Employee class 
  
string = "Someone-Unknown-1000"
emp_3 = Employee.from_string(string)

print(emp_3.pay)
print(emp_3.full_name())

# for staticmethod .

import datetime

day = datetime.date(2021 , 3 , 21)  

print(Employee.is_workday(day))
