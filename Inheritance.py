class product:
    def __init__(self,description):
        self.description = description
        
    def productDescription(self):
        print(self.description)
        
class lightProduct(product):
    max_weight_in_kgs = 5 
    
    def __init__(self,description,weight):
        self.weight = weight
        super().__init__(description)
        
    def validateWeight(self):
        return self.weight<=self.max_weight_in_kgs
pr = lightProduct('this is a 2 kg gym dumbell',2)
pr.productDescription()
        

    