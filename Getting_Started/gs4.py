class Car:
    color = 'White'

    def __init__(self):
        super().__init__()


# Deleting a property
c = Car()
print(c.color)
del c.color
print(c.color)
# we got error in second print statement because we have deleted color property