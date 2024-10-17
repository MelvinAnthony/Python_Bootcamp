#Problem 1
#Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
'''import math
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
            
    def distance(self):
        cal = math.dist(self.coor1,self.coor2)
        print(cal)
    
    def slope(self):
        m  = (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0]) 
        print(m)
        

# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance()
li.slope()
'''

#Problem 2

class Cylinder:
    pi = 3.14159
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        vol = Cylinder.pi*(self.radius**2)*self.height
        print(vol)
    
    def surface_area(self):
        sur = (2*Cylinder.pi*self.radius*self.height) + (2*Cylinder.pi*(self.radius**2))
        print(sur)

# EXAMPLE OUTPUT
c = Cylinder(2,3)
c.volume()
c.surface_area()