"""
operator overloading
-
"""

a = 5
b = 6
# using the int class method do the addition
c = int.__add__(a, b)
print(c)
print(a.__str__())
print(a) # here python automatically call str method in background
print("--------------------------------------")


# -------------------------------------------------

# Adding of two object using the add method

class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3

    def __mul__(self, other):
        m1 = self.m1 * other.m1
        m2 = self.m2 * other.m2
        s4 =Student(m1,m2)
        return s4

    def show(self):
        return self.m1, self.m2

    # using this method convert int to string
    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)





# create class object

s1 = Student(50, 60)
s2 = Student(60, 70)
print(s1.show(), s2.show())

# print the marks using string method

print(s1)  # if str method not define then it return the address of the object
print(s2)  # if str method define then it return the value store in object


# Addition of the two object using the add method
s3 = s1 + s2
print(s3)

# Multiphication of two object
s4 = s1 * s2
print("Multiphication ",s4)