# Implement a concept of multiple inheritance 

# Define class A
class A:
    # Method in class A to print "Hi"
    def sayHi(self):
        print("Hi")

# Define class B
class B:
    # Method in class B to print "Hello"
    def sayHello(self):
        print("Hello")
    
# Define class C inheriting from both A and B
class C(A, B):
    # Method in class C to print "Bye"
    def sayBye(self):
        print("Bye")

# Create an instance of class C
obj = C()
# Call method from class A
obj.sayHi()
# Call method from class B
obj.sayHello()
# Call method from class C
obj.sayBye()