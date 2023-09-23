class vehicle:
    def start_engine(self):
        print("starting_engine")
        
class car(vehicle):
    def __init__(self,make,model,year):
        super().__init__()
        self.make = ake
        self.model = model
        self.year = year
        
    def accelerate(self):
        print("accelrating")
        
    def break(self):
        print("braking")
        