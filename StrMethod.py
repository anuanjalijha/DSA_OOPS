class ocean:
    def __init__(self,sea_creature_name,sea_creature_age):
        self.name = sea_creature_name
        self.age = sea_creature_age
    
    def __str__(self):
        return f'The creature type is {self.name} and the age is {self.age}'
        
    def __repr__(self):
        return f'ocean(\'{self.name}\',{self.age})'
        
c = ocean('jellyfish',5)  
print(c)
print(str(c))
print(repr(c))