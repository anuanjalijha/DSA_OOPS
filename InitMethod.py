class product:
    count = 0
    def __init__(self,name,price,discount):
        self.id = product.count+1
        self.name = name
        self.price = price
        self.discount = discount
        self.isAvailable = True
        
        product.count+=1 
        
p1 = product('geaser',2000,0.05)
p2 = product('television',50000,0.2)

print(p1.__dict__)
print(p2.__dict__)
    
    
    