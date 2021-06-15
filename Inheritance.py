"""
-Inheritance : Acquired the property and behavior of the parent class in child class
-private members of super class not accessible in subclass


"""

class Polygon:
    #class variable

    __width = None
    __height = None

    def set_value(self,width,height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_heiht(self):
        return self.__height


class Rectangle(Polygon): # inherit Polygon class

    def area(self):
        return self.get_width() * self.get_heiht()



#create Rectanle class object

rect = Rectangle()

#using object access the super class method
rect.set_value(10,20)

print(rect.area())