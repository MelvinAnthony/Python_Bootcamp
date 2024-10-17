#Problem 1
#Handle the exception thrown by the code below by using try and except blocks.

'''try:
    for i in ["a","b","c"]:
        c = i**2
except:
    print("Invalid Option!")
else:
    print("Answer is: ",c)
finally:
    print("Always excute!!")
'''
#Problem 2
#Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

'''try:
    x = 5
    y = 0

    z = x/y
except:
    print("Invalid!")
finally:
    print("All Done")'''

#Problem 3
#Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
def ask():
    a = True
    while a:
        try:
            inp = int(input("Enter the integer: "))
            res = inp * 2
            print(f"The result is: {res}")
        except:
            print("Invalid input! Please enter an integer.")
        finally:
            ask_user = input("Do you want to continue? (yes/no): ").strip().lower()
            if ask_user == 'yes':
                a = True
            else:
                a = False

ask()
