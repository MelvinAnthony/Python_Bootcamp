#If, Elif, Else

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

# For Loop
'''#for loop using in operation

my_list = [1,2,3,4,5]
for i in my_list:
    print(i)

# for loop using range operation
for i in range(len(my_list)):
    print(i)
'''

#while Loop

'''x = 0

while x < 5:
    print(f"Your Current Value is {x}")
    x+=1

#using Break keyword
while x < 5:
    if x == 3:
        break
    print(f"Your Current Value using break keyword {x}")
    x +=1

#using Break keyword
while x < 5:
    if x == 3:
        continue
    print(f"Your Current Value using continue keyword {x}")
    x +=1
#using pass
while x < 5:
    def my(self):
        pass
print("this will excute by pass keyword")
'''

#using enumerate
l = ['a','b','c','d','e']
'''for key,value in enumerate(l):
    print(key)
    print(value)
    print("\t")
'''

#using zip operation
mylist1 = [1,2,3,4,5]
mylist2 = [100,200,300,400,500]

'''for i in zip(l,mylist1,mylist2):
    print(i)'''

#Using in operation
'''verify = 200 in mylist2
if verify == True:
    print("Yes 200 is present in mylist2")
    '''
#using random packages
'''from random import shuffle,randint

random_list = shuffle(mylist1)
print(mylist1)

print(randint(0,100))
'''
#using append operation
'''mylist = []
mylist.append(10)
print(mylist)'''

#using for loop comarssion in list square bracket
z = [i for i in mylist1]
print(z)

z = [i for i in mylist1]
print(z)

z = [i for i in range(0,10) if i%2==0]
print(z)

z = [i if i%2==0 else "ODD" for i in range(0,10)]
print(z)

z = []
for x in [1,2,3,4]:
    for y in [100,200,300,400]:
        z.append(x*y)
print(z)

z = [x*y for x in [1,2,3,4] for y in [100,200,300,400]] 
print(z)