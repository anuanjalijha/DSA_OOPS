class product:
    def __init__(self,description,price,discount):
        self.description = description
        self.price = price
        self.discount = discount
    
    def productDescription(self):
        print(self.description)
        
    def __calculateDiscount(self):
        return self.price-self.price*self.discount
        
    def getPrice(self):
        return self.__calculateDiscount()
        
        

class lightProduct(product):
    max_weight_in_kgs = 5 
    def __init__(self,description,weight,price,discount):
        self.weight = weight
        super().__init__(description,price,discount)
        
    def validateWeight(self):
        return self.weight<=self.max_weight_in_kgs
        
    def getPrice(self):
        self.price = self.price- self.price*0.15
        return super().getPrice()
    
pr = lightProduct('this is a 2 kg gym dumbell',3,400,0.1)
print(pr.getPrice())
