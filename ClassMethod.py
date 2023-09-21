class Employee:
    __company = 'Coding Ninjas'
    def __init__(self,id,name,salary):
        self.__id = id 
        self.name = name 
        self.__salary = salary 
        
    @staticmethod
    def greet():
        return "Have a great day!"
        
    @classmethod
    def intro(cls):
        return 'Welcome To '+cls.__company+'.'+cls.greet()
print(Employee.intro())        
        