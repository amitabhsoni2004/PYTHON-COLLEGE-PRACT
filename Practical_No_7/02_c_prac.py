# Implement a concept of hierarchy inheritance

# Define class A
class A:
    # Method to print "Hi"
    def sayHi(self):
        print("Hi")

# Define class B inheriting from class A
class B(A):
    # Method to print "Hello"
    def sayHello(self):
        print("Hello")
    
# Define class C inheriting from class A
class C(A):
    # Method to print "Bye"
    def sayBye(self):
        print("Bye")

# Create an instance of class B
obj_A = B()
# Call sayHi method from class A
obj_A.sayHi()
# Call sayHello method from class B
obj_A.sayHello()

# Create an instance of class C
obj_B = C()
# Call sayHi method from class A
obj_B.sayHi()
# Call sayBye method from class C
obj_B.sayBye()