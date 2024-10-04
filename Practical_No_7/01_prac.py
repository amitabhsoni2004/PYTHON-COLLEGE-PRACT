# Create a class that stores student data and display it

# Define the student class
class student:
    # Initialize the student object with name and roll number
    def __init__(self, name, roll):
        self.name = name  # Store the student's name
        self.roll = roll  # Store the student's roll number
    
    # Method to print student information
    def print_info(self):
        print(f"Your name is {self.name} and roll no is {self.roll}")  # Display the student's name and roll number

# Create an instance of the student class
s1 = student("Amitabh", 49)
# Call the method to print the student's information
s1.print_info()