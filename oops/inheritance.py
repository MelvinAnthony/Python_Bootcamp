# base inheritance
class myfirstclass():
    def __init__(self):
        print("Hi this was self class")
    def fun_first(self):
        print("this is my first fun!")
    def hi(self):
        print("Hi from first")
class mysecondclass(myfirstclass):
    def __init__(self):
        myfirstclass.__init__(self)

        print("HI this is my second self class")

    def sec_fun_first(self):
        print("this is my second class and first function")
    def hi(self):
        print("Hi from second")
    
c1 = myfirstclass()
c1.fun_first()
c1.hi()

