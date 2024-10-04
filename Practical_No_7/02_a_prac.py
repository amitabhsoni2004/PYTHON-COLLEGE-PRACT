# Implement a concept of single inheritance

# Define class A
class A:
    # Method in class A to print "Hello"
    def sayHello(self):
        print("Hello")

# Define class B that inherits from class A
class B(A):
    # Method in class B to print "Hi"
    def sayHi(self):
        print("Hi")

# Create an instance of class B
obj = B()
# Call the sayHello method from class A
obj.sayHello()
# Call the sayHi method from class B
obj.sayHi()