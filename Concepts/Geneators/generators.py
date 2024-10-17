'''def me(num):
    store = []
    if num > 0:
        for i in range(num):
            res = i**2
            store.append(res)
        return store
    else:
        return "Invalid Number!"

result = me(10)
print(result)
for x in result:
    print(x)'''
'''
def create_cubes(n):
    for x in range(n):
        yield x**3
print(list(create_cubes(10)))
'''

#function start,stop,step operations
'''
for i in range(1,20,2):
    print(i)
'''
'''
def me():
    for i in range(1,20,2):
        yield i
    
print(dict(me()))
'''

#Fibonanic series
'''
def fib_s(n):
    a = 1
    b = 1

    for i in range(n):
        yield a
        a = b
        b = a+b


for i in fib_s(10):
    print(i)
'''
#next function used
'''
def me():
    for i in range(10):
        yield i
    
call = me()

print(next(call))
for i in range(9):
    print(next(call))
'''

#iter function 
name = "melvin"
number = [1,2,3,4,5,6,7,8,9]

#for i in name:
#    print(i)

#print(next(number))
#print(next(name))

# it get error so using iter() function clear that 

name_iter = iter(name)
number_iter = iter(number)

def me():
    def name(na):
        for i in na:
            print(i)
    
    def number(num):
        for i in num:
            print(i)

    return type('', (), {'name': name, 'number': number})
call = me()
call.name(name_iter)
call.number(number_iter)



#
#name = "melvin"
#number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#name_iter = iter(name)
#number_iter = iter(number)
#
## Define the outer function
#def me():
#    # Define the inner function to print characters from name
#    def print_name(na):
#        for i in na:
#            print(i)
#    
#    # Define the inner function to print numbers from list
#    def print_number(num):
#        for i in num:
#            print(i)
#    
#    # Return both functions as a callable object
#    return type('', (), {'name': print_name, 'number': print_number})
#
## Call the me function to get the callable object
#call = me()
#
## Call the inner functions using the returned object
#call.name(name_iter)   # Will print characters of the name
#call.number(number_iter)  # Will print numbers from the list
#