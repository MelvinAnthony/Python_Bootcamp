# Polymorphism basic 

class one():
    def __init__(self,name):
        self.name = name

    def print_name(self):
        return f"Your name was in one {self.name}"

class two():
    def __init__(self,name):
        self.name = name
    
    def print_name(self):
        return f"Your name in two: {self.name}"

for display in [one,two]:
    #print(display)
    obj = display("melvin")
    obj.print_name()

def display_print(obj):
    return obj.print_name()

obj1 = one("melvin")
obj2 = two("Anthony")
print(display_print(obj1))
print(display_print(obj2))




