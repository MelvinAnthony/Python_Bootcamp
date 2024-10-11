# Error Expection Handling

'''try:
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    print(a+b)

except ValueError:
    print("Check the value give correct format is integer.")
else:
    print("I correctly excute the module")
finally:
    print("Final Statement alway run!!")
'''

def fun():
    try:
        a = int(input("Enter the input: "))
        b = int(input("Enter the input: "))
        c = a + b
        
    except:
        print("i get error :(")

    else:
        print("we added value")
        print(f"Result: {c}")
    finally:
        print("we add sucessfully!!")

fun()
