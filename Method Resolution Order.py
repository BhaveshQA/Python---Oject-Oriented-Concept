"""
MRO : It is defined the order of the method execution when there is multiple inheritance

"""

class A:

    def __init__(self):
        print("This is class A")


class B:

    def __init__(self):

        print("This is class B")


# Inherite two class, it also called Multiple Inheritance
class C(B,A):

    def __init__(self):
        super().__init__()
        print("This is class C")

        #when there is multiple inheritance then we can call init method forcefully using the class Name
        A.__init__(self)
        B.__init__(self)


# Create a  'C'class object

c1 = C()

#using the __mro__ we can get the method access order
print(C.__mro__)