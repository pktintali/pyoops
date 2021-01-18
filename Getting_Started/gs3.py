class Car:
    carColor = 'default'
    carWheels = 4
    carSpeed = 64

    def __init__(self, wheels, speed, color):
        self.carColor = color
        self.carWheels = wheels
        self.carSpeed = speed
        super().__init__()

    def display(self):
        print(self.carColor, self.carWheels, self.carSpeed)


c1 = Car(6, 100, 'black')
print(c1.carColor, c1.carWheels, c1.carSpeed)
# black 6 10

c2 = Car(4, 150, 'blue')
print(c2.carColor, c2.carWheels, c2.carSpeed)
# blue 4 150

#! Important Notes
# ? The self-parameter refers to the current instance of the class
# ? and accesses the class variables. We can use anything instead of self,
# ? but it must be the first parameter of any function which belongs to the class.