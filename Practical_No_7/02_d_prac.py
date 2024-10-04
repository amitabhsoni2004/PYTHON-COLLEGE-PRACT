# Implement a concept of Hybrid inheritance

# Base class A
class A:
    # Method in class A
    def sayHi(self):
        print("Hi.")
    
# Class B inherits from class A
class B(A):
    # Method in class B
    def sayHello(self):
        print("Hello.")

# Class C inherits from class A
class C(A):
    # Method in class C
    def sayContinue(self):
        print("Continue")

# Class D inherits from class B
class D(B):
    # Method in class D
    def sayChild1(self):
        print("Child 1")

# Class E inherits from class C
class E(C):
    # Method in class E
    def sayChild2(self):
        print("Child 2")

# Create an instance of class D
b = D()
b.sayHi()        # Call method from class A
b.sayHello()     # Call method from class B
b.sayChild1()    # Call method from class D

# Create an instance of class E
c = E()
c.sayHi()        # Call method from class A
c.sayContinue()  # Call method from class C
c.sayChild2()    # Call method from class E
