class MyClass:
    
    def __init__(self):
        self.__private_attribute = 30
        
    def __private_method(self):
        return "This is a private method"
        
obj = MyClass()
# Accessing private attribute and method using mangled names
print(obj._MyClass__private_attribute) # Output: 30
print(obj._MyClass__private_method()) # Output: This is a private method
