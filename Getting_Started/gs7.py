# getattr and setattr
class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
        super().__init__()


c = Car('Red', 100)
print(getattr(c,'color'))
setattr(c, 'color', 'blue')
print(c.color)