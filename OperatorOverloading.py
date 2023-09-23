class Number:
    def __init__(self,number):
        self.a =number
        
    def __add__(self,other):
        return self.a + other.a 

    def __mul__(self,other):
        return self.a * other.a 
        
        
a = Number(3)
b = Number(5)
print(a+b)
print(a*b)
        