class user:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        
class customer(user):
    def __init__(self,name,email):
        super().__init__(name,email)
        self.cart = []
    
    def add_to_cart(self,item):
        self.cart.append(item)
        
class premiumCustomer(customer):
    def __init__(self,name,email):
        super().__init__(name,email)
        self.discount = 0.1 
        
    def apply_discount(self,price):
        return price*(1-self.discount)
        
    
    