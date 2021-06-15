"""
super() : using this function we can call super class init method
"""

class Parent:

    def __init__(self):
        print("This is parent class")


class Child(Parent):

    def __init__(self):
        print("This is child class")
        super().__init__()  # this will call the Parent class init method

# create child class object
c = Child()
