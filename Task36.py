'''Write a program to create an abstract class Animal with an abstract method 
called sound(). Create subclasses Lion and Tiger that extend the Animal class 
and implement the sound() method to make a specific sound for each animal.'''

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Lion (Animal):
    def sound(self):
        print("The lion roars")

class Tiger (Animal):
    def sound(self):
        print("The Tiger growls")

lion =Lion()
lion.sound()

tiger = Tiger()
tiger.sound()