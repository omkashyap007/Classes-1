""" The magic mehtods are special methods whcih have double 
underscores at the begining and at the end .

They are also called dunders .

__init__ is a constructor but is a dunder .
__add__ is a dunder .

"""
class Vector2D:
    def __init__(self , x , y) :
        self.x = x
        self.y = y 

    def __add__(self , other) :
        return Vector2D(self.x + other.x , self.y + other.y)

first = Vector2D("no" , "talking")
second = Vector2D("more" , "useless")

result = first + second

print("\n\n")
print(result.x)
print(result.y)

print("\n\n")

print(first + second)
print("\n\n")


"""
well here the dunders like __add__ are used to make the complex 
calculations like + , - , * , / easier on the basis of the objects.
On the basis of objects .

it means , what if you divide mgr_1 / dev_2 , WTF will be the 
output .
the functions (dunders ) assigned to the classes do the same thing
as +  , - , * , / do , but for the objects .

these dunders are very helpfull when you work with objects .



when two objects are added . the python may won't know what will
be the data type , int , float , string . 

the added up objects gives the class .

hence these dunders make the calcualtions easier .

"""

# dunders
#  print((x).__add__(y))


class strings:
    def __init__(self , string ):
        self.string = string 
    
    def __truediv__(self , other):
        line =  len(other.string )
        print(self.string,"\n" ,line*"-","\n" , other.string )

a = strings("Something")
b = strings("Nothing")
print(a/b)


"""
The dunders come to aciton when they see that theres an mathematical
operation on the classes .

so if you cretaed a dunder to add and then  you add the objetcs , 
the dunder which corresponds to the calculation gets used .

like here i divided ( a / b ) . the a and b are the obejct of the 
stirings class . how can you apply the division for the classes .

so the dunder makes the entry and when the division operator is applied
on the objects . the dunder comes to action and the  __add__ function is 
run , and the code lines which are setup start to work .

"""




print((10).__add__(9))
print((10).__sub__(9))
print((10).__mul__(9))
print((10).__truediv__(9)) # for / ( dividing) 
print((10).__floordiv__(9)) # floor division //
print((10).__mod__(9))    # for %
print((10).__and__(9))    # for &
print((10).__xor__(9))
print((10).__or__(9))       
