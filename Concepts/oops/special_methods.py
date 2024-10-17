#Special methods

class one():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self): # it display the string value not store value
        return f"{self.name} and {self.age}"
    def __len__(self):
        return self.age
    def __del__(self):
        print("Objet was deleted")
    
c1 = one("melvin",23,"male")
print(c1)
print(len(c1))
del c1

