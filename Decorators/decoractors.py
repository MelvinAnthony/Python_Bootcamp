'''def me():
    return "hello"
another_way = me

print(another_way())

del me

print(another_way())
print(me())
'''
#function inside the function how we call
'''
def hello(name = "melvin"):
    print("The hello() Function has been executed")

    def greet():
        return "this is greet()"
    def welcome():
        return "this is welcome()"
    
    if name == "melvin4":
        return greet
    else:
        return welcome
my = hello("melvin")
print(my())
'''

'''def cool():
    def super_cool():
        return "It is super cool"
    return "I am going to super_cool() \n"+super_cool()
my = cool()
print(my)'''


'''def hello():
    return "Hi melvin"

def wel(hello_fun):
    print("It was another function")
    print(hello())

wel(hello)'''


#using @Decorator method 


def original_func():
    return "hi this is original func!"

# Correct decorator with function passed as argument
def new_decorator(func):
    def wrap_func():
        print("It was run before calling the function!")

        print(func())  # Call the original function passed to the decorator

        print("After the function has been called!")
    
    return wrap_func

# Manually using the decorator
fun1 = new_decorator(original_func)
fun1()

# Using the decorator syntax
@new_decorator
def decorator():
    return "This was run by the decorator function!"

decorator()  # Now this will work correctly



