class Employee:

    def __init__(self , first , last , pay):
            self.first = first 
            self.last = last
            self.pay = pay
            
    # __init__ is constructor .
    # this is called when an instance is created .

    # __init__ is the constructor which is used to create instances and arguments.
    # the first , last and pay are called the arguments .
    # the variables defined in the __init__ fucntion are called arguments ..

    # self here is bascially an insatnce ..
    # writing emp_1.first = first  .. is same are self.first = first
    # in the class ...
    
        
    def full_name(self):
        return "{} {}".format(self.first , self.last)
    
    # self is the instance . so when this functoin is called . 
    # the self is replaced with the variable name.


    # full_name is a method in the class .
    # the functions defined insdie the class are called methods.
    # all methods should have self argument in it. 



emp_1 = Employee("Om" , "Kashyap" , 100000) 
# emp_1 is the instances , the varables using the class are called instances

print(emp_1.full_name())
# well this can also be achieved using the Employee class
print(Employee.full_name(emp_1))
# whent the method is called on the class we need to pass the instance.
