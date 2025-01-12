# Outline: Write a program to create a class Parrot
#  and perform the following tasks - 
# Create a class variable species
#  Create a __init__ method that has instance variables - name and age 
# Create instances of class Parrot, passing arguments as well Print Class variable by accessing it 
# Print Instance variables as well


class Parrot:
    #class variable
    species="Bird"

    def __init__(self,name,age):
        #instance variables
        self.name=name
        self.age=age

p1=Parrot("Rio",2)
p2=Parrot("Blu",3)

print(p1.name," is a ",p1.species)
print(p2.name," is a ",p2.species)

print(p1.name," is a ",p1.age," years old")
print(p2.name," is a ",p2.age," years old")

