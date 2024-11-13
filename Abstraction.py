from abc import ABC , abstractmethod
#ABstract class
class  Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")  
#Using the abstract class
def Animal_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()
Animal_sound(dog)
Animal_sound(cat)