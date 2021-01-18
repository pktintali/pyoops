# inheritance
class Animal:
    def speak(self):
        print('Animal Speaking')


class Dog(Animal):
    def bark(self):
        print('Barking')


d = Dog()
d.bark()
d.speak()