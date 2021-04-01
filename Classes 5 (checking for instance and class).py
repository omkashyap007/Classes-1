class Employee:

    raise_amount = 1.04
    def __init__(self , first, last , pay ) :
        self.first = first 
        self.last = last 
        self.pay = pay
        self.email  ="{}.{}@email.com".format(self.first , self.last)

    def fullname(self) :
        return "{} {}".format(self.first , self.last)

    @classmethod 
    def from_string(cls , string) :
        first , last , pay = string .split("-")
        return cls(first , last , pay) 


class Developer(Employee):

    no_of_devs = 0 

    def __init__(self , first , last , pay , prog_lang) :
        super().__init__(first , last , pay) 
        self.prog_lang = prog_lang

        Developer.no_of_devs +=1 

    def total_devs(self) :
        return Developer.no_of_devs 

class Manager(Employee):

    def __init__(self , first , last , pay , employees = None):
        super().__init__(first , last , pay )
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self , emp):
        if emp in self.employees:
            pass
        if emp not in self.employees:
            self.employees.insert(0 , emp)


    def remove_emp(self , emp) :
        if emp in self.employees:
            self.employees.remove(emp)
        
    def print_emps(self) :
        for emp in self.employees:
            print("-->" ,emp.fullname())
        
dev_1 = Developer("OM" , "Kashyap" , 1000000 , "Python")
dev_2 = Developer("Someone" , "Unknown" , 1000 , "Java") 
dev_3 = Developer("Aman" ,"Gupta" ,800000 , "C++")

mgr_1 = Manager("No" , "One" , 3042304 ,[])

mgr_1.add_emp(dev_1) 
mgr_1.add_emp(dev_2)
mgr_1.add_emp(dev_3)

print(mgr_1.print_emps())

mgr_1.remove_emp(dev_2) 

print(mgr_1.print_emps())

print(isinstance(mgr_1 , Manager))
print(isinstance(mgr_1 , Employee))
print(isinstance(mgr_1 , Developer))
print(isinstance(dev_1 , Developer))
print(isinstance(dev_2 , Manager))
print(isinstance(dev_3 , Employee))

print("\n")

print(issubclass(Manager , Employee))
print(issubclass(Developer,  Employee))
print(issubclass(Developer , Manager))
print(issubclass(Manager , Employee))
