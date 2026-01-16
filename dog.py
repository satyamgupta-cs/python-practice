class Dog:
    def __init__(self , name , age):
        self.name = name 
        self.age = age 
    
    def sit(self):
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        print(f"{self.name} roll over.")

my_dog = Dog('willie', 9)
print(f"my dog's name is {my_dog.name}")
print(f"his age is {my_dog.age}")
my_dog.sit()
my_dog.roll_over()
