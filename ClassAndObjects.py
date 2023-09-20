class product:
    company = 'Adidas'
    def printCompany(self):
        print(self.company)
        
class cart:
    maxsize = 50 
    
    def printCartSize(self):
        print(self.maxsize)
p1 = product()
print(p1.company)
p1.printCompany()
c1 = cart()
c1.printCartSize()