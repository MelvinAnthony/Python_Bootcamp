#demo class creation get the user input for name,age,gender and print the value
class my():
    current_location = "chennai"
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender       

    def me(self):
            
        print(f"My name was {self.name} and age of my was {self.age} and i am a {self.gender} and current location was {my.current_location}")


name = input("Enter your name: ") 
age = int(input("Enter the Age: "))
gender = input("Enter your gender: ")

person = my(name,age,gender)

person.me()