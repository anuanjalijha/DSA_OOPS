class shape:
    def calculate_area(self):
        pass
        
class rectangele(shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width*self.height
        
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
        
    
    def calculate_area(self):
        return 3.14*self.radius**2

class triangle(shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return 0.5*self.base*self.height
        

    
    