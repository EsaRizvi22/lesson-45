# Write a program to create a class with name Student and perform the following tasks - Create a class variable grade and name 
# Create a function to print a sentence 
# Create a function to print class variables grade and name 
# Create an object of class Student 
# Call the two functions to execute them

class student:
    #class variables
    grade=10
    name="Ali"

    def show(self):
        print("Welcome to my first class method")
    def display(self):
        print("Name of the student is ",self.name," and grade is ",self.grade)

st1=student()
st1.show()
st1.display()
