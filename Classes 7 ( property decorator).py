class Employee:

    raise_amount = 1.04

    def __init__(self , first , last , pay ) :
        self.first = first 
        self.last = last 
        self.pay = pay
#       self.email = "{}.{}@email.com".format(self.first , self.last)   
    
    @property
    def email(self) :
        return "{}.{}@email.com".format(self.first , self.last) 

    @property
    def fullname(self):
        return "{} {}".format(self.first , self.last)

    @fullname.setter
    def fullname(self , name):
        first , last = name.split(" ")
        self.first = first 
        self.last = last
    @fullname.deleter
    def fullname(self ):
         print("Deleted !")
         self.first = None 
         self.last = None

"""
if you want to change the name of the object .
or if you want to set the first , last and name of the object.


 use the setter property, the setter uses property function name (here fullname)
@fullname.setter

if you want to set something from the fullname


""" 
    



emp_1 = Employee("Om" , "Kashyap" , 100000)

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

print("\n\n")

emp_1.first = "Aman"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# the email still gives the first name to be Om not Aman .
# adding the function 
"""
def email(self):
    return "{}.{}@email.com".format(self.first , self.last)

but this would change the whole code and parantheses must be applied to access the email.


hence if you want to access the email with the updated name and other information

create a function email and write @property above that.

THEN YOU CAN ACCESS THE FUNCTION (METHOD) AS A ATTRIBUTE
attribute is the property of the object .
"""

# for the setter

emp_1.fullname = "Aman Gupta"

print(emp_1.fullname)

# with the properties you can change the access ways of the method to the attribute.
#  and can change the object properties using the property decorator .
# 

print(emp_1.first )
print(emp_1.last)


# using the deleter 

del emp_1.fullname
