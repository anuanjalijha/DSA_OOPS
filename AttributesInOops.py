class product:
    company = 'Adidas'
    def __init__(self,id,company):
        self.id =id
        self.company = company 
    def printCompany(self):
        print(self.company)
        


p3 = product(1,'ADIDAS-ABC')
p4 = product(1,'ADIDAS-XYZ')
print(p3.company)
print(p4.company)
print(product.company)
class dog:
    def __init__(self):
        print('self from init', id(self))
do = dog()  
print('id from outide', id(do))



