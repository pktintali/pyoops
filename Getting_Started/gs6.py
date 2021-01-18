class Car:
    # Parameterized Constructor
    def __init__(self,name,speed):
        self.name=name
        self.speed =speed
        super().__init__()
    def display(self):
        print(self.name,self.speed)


c = Car('BMW',200)
c.display()