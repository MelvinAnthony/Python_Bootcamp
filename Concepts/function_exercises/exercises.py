#Exercise 1: Create a function in Python
#Write a program to create a function that takes two arguments, name and age, and print their value.

'''def create(name,age):
    print(f"Your name: {name} and Age: {age}")


create(name = input("Enter the name: "), age = int(input("Enter the age: "))) '''

#Exercise 2: Create a function with variable length of arguments
#Write a program to create function func1() to accept a variable length of arguments and print their value.

#Note: Create a function in such a way that we can pass any number of arguments to this function, and the function should process them and display each argument’s value.

def func1(*args):
    name = args[0]
    age = args[1]
    location = args[2]
    print(f"Name of the user: {name} Age of the user: {age} and current location: {location}")

func1(input("Enter the name: "),int(input("Enter the age: ")), input("Enter the Location: "))

