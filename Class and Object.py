"""
class :it contains attributes and method , it is blue print
attributes >> variable and its data
method >> action performed on data
"""

"""
object : It is real world entity which we create while access the class attribute and method
-When class object created then actual memory allocation done for the class variable data
-Every object system create new copy of the variable
"""

"""
Self :It is default variable which store the memory address of the current object
-it is the first argument of any object method
-self keyword mandatory is while the access the variable
"""

# Example 1

class Myclass(object): # object is not mandatory to pass. it consider as class derived from the Base class

    def show(self):
        print("This is the class method")


m = Myclass() # Create object of the class
m.show() # using the object we can access the class method

print("---------------------------------------------------")

#------------------------------------------------------------
# Example 2 : without object parameter in class name

class Myclass2:

    def show(self):
        print("My Class2 method")


m1 = Myclass2()
m1.show()

print("---------------------------------------------------")

#-----------------------------------------------------------------

# example 3

class Mobile():

    def __init__(self):  # this is special method, constructor, auto-called once class object created
        self.model = 'realme'

    def show(self):
        print("Mobile Model:",self.model)


mobile = Mobile()
mobile.show()  # using object access class method

print(mobile.model)  # using the object direct access the variable

# we can also change the variable value
mobile.model = 'Samsung'
print(mobile.model)

print("--------------------------------------------------")

# Exmple 4

class Car:

    def __init__(self,model):
        self.car_model = model

    def model_price(self):
          self.price = 1000  # if we define this way then it accessible in other method
          price = 500   # this is local variable

          print("Model :", self.car_model, "Price :", price)

    def show(self):
        print("Model :",self.car_model, "Price :", self.price)


# create classs object
car = Car("Creta") # pass actual parameter
car.model_price()
car.show()

print("----------------------------------------------------")

#---------------------------------------------------------------

# contructor call = No of Instace created of the class

class test:

    def __init__(self):
        print("Calling the Contructor")



# create instance of the class

t1 = test()
t2 = test()
t3 = test()


print("-------------------------------")

# 'self' keyword
# Python not allowed to create multiple __init__(self) method in class
class Check:

    def __init__(self):
        print(id(self))  # self variable id and Object id is same.


c1 = Check()
print(id(c1))

c2 = Check()
print(id(c2))


print("-----------------------------------------------------")

#------------------------------------------------------------

class Computer:

    def __init__(self,brand,price):
        self.brand = brand
        print("Brand :",brand)
        print("Price :",price)



# create instace of computer class

com1 = Computer("Dell", 35000)

# Access using the object
print(com1.brand)  # we can only get variable if it assigned with self