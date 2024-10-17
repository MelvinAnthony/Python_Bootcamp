#String
'''a = "Here you are specifying that you want the characters from index 1, which is the second character of your string, till the last index at the end."
#a[0] = "W"
print(a[:])
print("---------------------------")
print(a[0:-1])
print("---------------------------")
print(a[1::3])
print("---------------------------")
print(a.split("e"))
print("---------------------------")
print(a.upper())
print("---------------------------")
print(a.lower())

#print formating

name = "melvin" 
age = 23
degree = "M.tech"

#two types of formating (.fromat, f - string)
#using .fromat 
print("student name is {} and student age is {} and degree {}".format("melvin", "23", "M.tech"))

# f - string
print(f"student name is {name} and student age is {age} and degree {degree}")
'''

#List
'''a = [1,2,3.98,4,5,"melvin"]
print(a)

#merge the new list

b = [9,8,7,6]
c = a+b
print(c)
print(c[::-1])

#usig indexing add
c[0] = "Anthony"
print(c)

#using append add the values
c.append("Arul")
print(c)

#pop
c.pop()
print(c)

print(c.sort())'''

#dictionary
'''d1 = {"s1":"melvin","s2":"Anthony"}
#print(d1["s1"])

d2 = {
    "s1":{
    "name":"melvin",
    "age": 23,
    "course":["python","machine learning"]
    },
    "s2":{
        "name":"Anthony",
        "age": 18
    }
}

search = d2["s1"]['course']
print(search[0].upper())

#search what are the key we have
print(d2.keys())

#search what are the values we have
print(d2.values())

#search what are the items we have
print(d2.items())
'''

#Tuple
'''t = ('a','b',123)
print(t)

#using count operation
tu = ('a','b','a','c','b',123)
print(tu.count('a'))

#using index operation
print(tu.index(123))

a1 = (123,[12])
print(type(a1))
'''

#Sets
'''s = set()
s.add(1)
s.add(1)
list = [1,2,3,4,5,6,1,2,3,4,5,6]
myset = set(list)
s.add(2)
print(myset)
print(set('Mississippi'))

s2 = set([1,2,1])
print
'''


#Boolean
'''def fun(value):
    if 1 > 2:
        return False
    else:
        return True
print(fun(1))
'''

#comparsion chain operator and If, Elif, Else

'''def me(value):
    if value == 5 and value < 3:
        print("Use AND Condition")
    elif value == 5 and value < 10:
        print("Using OR operation")
    elif not 11 == 11:
        print("using NOT operation")
    else:
        print("NO output")
print(me(11))
'''
