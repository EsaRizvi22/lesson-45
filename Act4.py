# Write a program to create a class Parrot and perform the following tasks - 
# Create a class variable species Create a constructor that has instance variables - name and age 
# Create instance methods for this class named sing and dance, making them print a message. 
# Create instances of class Parrot, passing arguments as well Print Class variable by accessing it Print Instance variables as well



class Parrot:
    #class variable
    species="Bird"

    #constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
#instance method
    def sing(self,song):
       return "{} sings {} song ".format(self.name,song)

    def dance(self):
       return self.name," is dancing now"


p1=Parrot("Rio",2)
print(p1.name ,"is a ",p1.species," and is ",p1.age," years old")
print(p1.sing("happy"))
print(p1.dance())
