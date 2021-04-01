# INHERITENCE .

# inheriting the arguments and the mehtods from the Employee class .

# creatrintg two classes developer and the manager .

class Employee:

    raise_amount = 1.04

    def __init__(self , first , last , pay ) :
        self.first = first 
        self.last = last 
        self.pay = pay 

    def full_name(self) :
        return "{} {} ".format(self.first , self.last ) 

    def apply_raise(self) :
        self.pay = int(self.raise_amount * self.pay)

        # the rasie_amount should be "self".raise_amount .
        # because , the self.raise_amount can have the raise_amount 
        # from different classes .

        # Employee.raise_amount can only have the raise_amount only from
        # the Employee class

    @classmethod 
    def set_raise_amount(cls , amount) :
        cls.raise_amount = amount 

    @classmethod 
    def from_string(cls , string ) :
        first , last , pay = string.split("-")
        return cls(first , last , pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6 :
            return False
        return True

# here we create two different type of employees like Developer and the
# Manager. 

class Developer(Employee) :
    raise_amount = 2

    def __init__(self , first , last , pay , prog_lang) :
        super().__init__(first ,last ,pay)
        self.prog_lang  = prog_lang

        # every method have __init__ method .
        # the one extra attribute is prog_lang
        # let the Employee class handle other attributes like first , last


        # now we want to get all the atributes in the parent class
    #first way .probaly better one .
        # when use super dont use self . 
        

    #second 
        # whe using Employee . use self .
#       Employee.__init__(self , first , last , pay , prog_lang)


    # the Developer class inherited all the methods , attributes from the 
    # Employee class .

    # now we want to get all the atributes in the parent class
    
    #first way .probaly better one .
   
   #second 
   #  Employee.__init__(self , first , last , pay , prog_lang)

    
dev_1 = Developer("Om" , "Kashyap " , 10000000 ,"Python")
print(dev_1.pay)
dev_1.apply_raise() 
print(dev_1.pay)
print(dev_1.prog_lang) 

# first the developer class found out the __init__ method in the 
# Developer class and then in the class from which it is 
# inherited .


# it looks through the chain of inheritence . 
# this chain is called METHOD RESOLUTION ORDER. 

# means  -:  Developer >> Employee .


# the answer would be same as creating an emloyee ... 

# to see the Method Resolution order

 # print(help(Developer))


dev_2 = Developer("Test" , "Person" , 20000 , "Java")
print(dev_2.pay) 
dev_2.apply_raise() 
print(dev_2.pay)
print(dev_2.prog_lang)


emp_1  = Employee("New" , "Person" , 30000)

# no programming language
# theres the difference between the employee class and the Developer 
# class .
