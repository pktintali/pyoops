class Car:
    carColor = 'default'
    carWheels = 4
    carSpeed = 64

    def __init__(self, wheels, speed, color):
        # TODo Update properties
        super().__init__()

    def display(self):
        print(self.carColor, self.carWheels, self.carSpeed)


c = Car(6, 100, 'black')
print(c.carColor, c.carWheels, c.carSpeed)
# Here we didn't update the class properties thats why we are getting default value
# default 4 64

#!important Notes
# ? Here, the self is used as a reference variable,
# ? which refers to the current class object.
# ? It is always the first argument in the function definition.
# ? However, using self is optional in the function call.
