class product:
    def __init__(self,description):
        self._description = description
        
        
class lightProduct(product):
        
    def getDescription(self):
        return self._description
pr = lightProduct('this is a 2 kg gym dumbell')
print(pr.getDescription())
        

    