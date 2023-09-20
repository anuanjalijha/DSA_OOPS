class product:
    company = 'Adidas'
    def __init__(self,id):
        self.id =id
    def printCompany(self):
        print(self.company)
        
class cart:
    count  = 0 
    
    def __init__(self,id,name):
        cart.count = cart.count+1
        self.id =id
        self.name = name

    def printCartSize(self):
        print(self.maxsize)
p1 = product(1)
p2 = product(2)
print(p1.id) 
print(p2.id)
cart1 = cart(1,'cart1')
cart2 = cart(2,'cart2')
cart3 = cart(3,'cart3')
print(cart.count)
print(cart1.count)
print(cart1.id) 
print(cart2.id)
print(cart1.__dict__)
# other way of dict 
print(vars(cart2))



