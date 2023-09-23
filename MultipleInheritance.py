class phone:
    def make_call(self):
        print("making calls")
    
    def send_messages(self):
        print("sending messages")

class computer:
    def browse_internet(self):
        print("browsing internet")
    
    def send_mail(self):
        print("sending mail")
        
class smartPhone(phone,computer):
    def __init__(self,model,year):
        super().__init__()
        self.model = model
        self.year = year