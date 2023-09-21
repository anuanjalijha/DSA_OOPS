class Employee:
    __company = 'Coding Ninjas'
    def __init__(self,id,name,salary):
        self.__id = id 
        self.__name = name 
        self.__salary = salary 
        
    
    def employeeDetails(self):
        return 'Name:'+self.__name+'\nId: '+str(self.__id)+'\ncompany: '+self.__company
    
emp1 = Employee(1,'Raman',40000)
emp2 = Employee(2,'suman',50000)
print(emp1.employeeDetails())
print(emp2.employeeDetails())

        