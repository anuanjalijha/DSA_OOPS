class Animal:
    def speak(self):
        print("animal soeaking...")
        
class Dog(Animal):
    def speak(self):
        print("woof...")
        
class cat(Animal):
    def speak(self):
        print("meow...")
    
c = cat()
d = Dog()
c.speak()
d.speak()