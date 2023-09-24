class MyClass:
    
    @staticmethod
    def static_method():
        print("This is a static method")

# Calling static method using class name
MyClass.static_method()
# Calling static method using an instance
obj = MyClass()
obj.static_method()