"""
-In python we don't have direct option to declare class and method as abstract
-we need to import in-built library function
-

"""
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def test1(self):
        pass

    @abstractmethod
    def test2(self):
        pass


class B(A):

    def test3(self):
        print("Test 3 Normal method")

    def test1(self):
        print("Abstract method implemtation")


    def test2(self):
        print("Abstract method test2 implementation")

# Can't create object of the Absract class
# a = A()

b = B()
print(b.test3())
print(b.test2())
print(b.test1())