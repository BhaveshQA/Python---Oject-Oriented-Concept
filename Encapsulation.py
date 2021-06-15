"""
-Encapsulation in Python is the process of wrapping up variables and methods into a single entity
-wrapped data is not possible by any code defined outside the class in which the wrapped data are defined.
-Encapsulation provides security by hiding the data from the outside world.
-If we declare any variable or method as private, then they can be accessed only within the class
 in which they are defined
-private members are preceded by two underscores
-private members are accessed only inside the class and its method
"""


class Hello:

    def __init__(self):
        self.a = 10
        self._b = 20  # semi private
        self.__c = 30  # declare private

    def public_method(self):
        print("Private member in other method :", self.__c)  # private member access any function of that class
        self.__private_method()  # using the self variable we can access the private method

    def __private_method(self):  # private method
        print("This is private method")


# create class object
h1 = Hello()
print(h1.a)  # we only access a data member directly
h1.public_method()

print("-------------------------------------------")


# -------------------------------------------------

class Car:

    def __init__(self, model, speed):  # this behave as constructor and initialize the variable
        self.__model = model
        self.__speed = speed

    def set_model(self, model_value):  # this set the value to variable
        self.__model = model_value

    def set_speed(self, speed):
        self.__speed = speed

    def get_model(self):  # this return the value to setter method
        return self.__model

    def get_speed(self):
        return self.__speed


# create object of class

car = Car("Scorpio", 200)
print(car.get_model(), car.get_speed())

# car.__model we cannot use this as variable is private
car.set_model("Honda")  # we can update value using only the function

print(car.get_model())
