class BankAccount:
    def __init__(self,balance):
        self.balance = balance
        
    def deposit(self,amount):
        self.balance+=amount
        
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("Insufficient balance")
            
            
class SavingAccount(BankAccount):
    def __init__(self,balance,interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate
        
    def calculate_interest(self):
        return self.balance*self.interest_rate
        
class CreditCard(BankAccount):
    def __init__(self,balance,credit_limit):
        super().__init__(balance)
        self.credit_limit = credit_limit
        
    def make_purchase(self,amount):
        if self.balance+self.credit_limit>=amount:
            self.balance-=amount
        else:
            print("credit limit exceeded")
            
class StudentAccount(StudentAccount,CreditCard):
    def __init__(self,balance,interest_rate,credit_limit,student_discount):
        SavingAccount.__init__(self,balance,interest_rate)
        CreditCard.__init__(self,balance,credit_limit)
        self.student_discount = student_discount
        
    def applyDiscount(self,price):
        return price*(1-self.student_discount)
    
        
        
        