class Animal:
    def speak(self):
        return "hayvans ses cikarir"
class Dog(Animal):
    def speak(self):
        return "hav hav"
class Cat(Animal):
    def speak(self):
        return "miyav"

animals=[Dog(), Cat()]
for animal in animals:
    print(animal.speak())