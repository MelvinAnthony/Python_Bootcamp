#functions
'''def my_fun(self):
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))

    return name + age
my_fun()
'''

#function give as default value
'''
def fun(name="me"):
    print(f"Name: {name}")
fun("melvin")
'''

#function using logic
'''def num_check(number):
    if number %2 ==0:
        return f"It was even number: {number}"
    else:
        return f"It is add number: {number}"
    
num = int(input("Enter the number: "))
print(num_check(num))'''

'''def fun(num):
    if num %2 ==0:
        return f"It was even number: {num}"
    return False
print(fun(4))
'''

#find the employee check who work more time using function

'''emp = [("melvin",100),("Anthony",200),("Arul",300),("Raj",50)]

def check(emp):
    current_max = 0
    current_emp = ''
    for emp,hour in emp:
        if hour > current_max:
            current_max = hour
            current_emp = emp
        else:
            pass
    return (f"Who was the employee: {current_emp} and working hour is: {current_max}")
print(check(emp))

hours = check(emp)

print(type(emp))
'''
#function using shuffle game
'''from random import shuffle
my_list = [1,2,3,4,5,6,7]

def suffle_list(my_suffle):
    shuffle(my_suffle)
    return my_suffle
print(suffle_list(my_list))
'''
'''my_list = [1,2,3,4,5,6,7]
def player_guess(num):
    guess = ''
    while guess not in my_list:
        print("it was not present")
    return int(guess)
print(player_guess(2))
'''
#Using *args in functions it create a n number of paramenter in the paranthesis - it return back as tuple

'''def myfun(*args):
    final = sum(args) * 0.05
    return final
print(myfun(10,20))

def myfun(*melvin):
    final = sum(melvin) * 0.05
    return final
print(myfun(10,20))
'''

#Using **kwargs in functions it create a n number of paramenter in the paranthesis - it display as key value pairs like dictionary

'''def myfun(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print("Fruit name was: {}".format(kwargs['fruit']))
        print(f"Fruit name was: {'fruit'}")
    
myfun(fruit = "apple")
'''

#combine code of *args and **kwargs

'''def myfun(*args,**kwargs):
    print(args)
    print(kwargs)
    print("I like a {} {}".format(args[0],kwargs['food']))
myfun(10,20,30,food = "Briyani", play = "cricket")
''' 

# Map method
num_list = [1,2,3,4,5]
'''def map_check(num):
    return num*2
for i in map(map_check,num_list):
    print(i)

print(list(map(map_check,num_list)))

def splicer(mystring):
    if len(mystring)%2 == 0:
        print("Even")
    else:
        print("ADD")

mylist = ["melvin","Anthony"]

list(map(splicer,mylist))
'''

#filter function
'''def filter_fun(num):
    if num%2==0:
        print(num)
    else:
        pass
list(filter(filter_fun,num_list))
'''

#lambda function
num_list = [1,2,3,4,5]
'''square = lambda num: num**2

print(square(5))

print(list(map(lambda num : num**2,num_list)))

name_list = ["melvin","Anthony"]

c = list(map(lambda reverse_list: reverse_list[::-1],name_list))
print(c)
'''

#Local veraible declare using LEGB formula

#Global
'''name = "melvin"
def me_fun():
    #Enclosing
    name = "Anthony"
    
    def hello():
        #local
        name = "Arul"
        print(f"Hi: {name}")
    hello()
me_fun()
me_fun()
'''
# function using create a global variable in local or inside function

'''x = "melvin"
def function(x):

    print(f"Hi: {x}")

    x = "Anthony"
    print(f"hi: {x}")

function(x)
'''

#create a X and O game
'''def xo_play(*args):
    print(row1)
    print(row2)
    print(row3)

row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

getuser = int(input("Enter the where you want place options 0,1,2: "))
getvalue = input("Enter the value x or O: ")
row1[getuser] = getvalue
xo_play()'''

def digit(*args):
    getuser = input("Enter the where you want place options: ")

    while getuser.isdigit() == False:
        getint = input("Give the numeric input: ")

        if getint.isdigit() == True:
            
            print(f"number is: {getuser} and numberic place was {getint}")
digit()