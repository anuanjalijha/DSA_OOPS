class computer:
    def __init__(self):
        self.name = 'computer'
    def __del__(self):
        print('destructor called')  
def fun():
    c = computer()
fun()
print('computer')          