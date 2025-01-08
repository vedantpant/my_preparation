# class Dog:
#
#     def __init__(self, name):
#         self.name = name
#
#     def display_name(self):
#         print(f"Dog name: {self.name}")
#
#
# class Labrador(Dog):
#
#     def sound(self):
#         print("Labrador sound")
#
#
# class GuideDog(Labrador):
#     def guide(self):
#         print(f"{self.name}guides the way")
#
#
# class Friendly:
#
#     def greet(self):
#         print("Friendly dog")
#
#
# class GolderRetriever(Dog,Friendly):
#
#     def sound(self):
#         print("Golder Retriever sound")
#
#
# lab = Labrador("Buddy")
# lab.display_name()
# lab.sound()
#
# guide_dog = GuideDog("Tommy")
# guide_dog.display_name()
# guide_dog.sound()
# guide_dog.guide()
#
# retriever = GolderRetriever("Max")
# retriever.display_name()
# retriever.sound()
# retriever.greet()

# class Dog:
#
#     def sound(self):
#         print("dog sound")
#
#
# class Labrador(Dog):
#
#     def sound(self):
#         print("Labrador sound")
#
#
# class Beagle(Dog):
#     def sound(self):
#         print("Beagle sound")
#
#
# dogs = [Dog(), Labrador(), Beagle()]
#
# for dog in dogs:
#     dog.sound()
#
# class Calculator:
#
#     def add(self,a,b):
#         return a+b
#
#     def sub(self,a,b):
#         return a-b
#
#     def mul(self,a,b):
#         return a*b
#
#     def div(self,a,b):
#         return a/b
#
# calc = Calculator()
# print(calc.add(1,2))

# class Dog:
#
#     def __init__(self,name,age,bread):
#         self.name = name
#         self.__age = age
#         self._bread = bread
#
#     def get_info(self):
#         return f"Name: {self.name}, Age: {self.__age}, Bread: {self._bread}"
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         if age > 0:
#             self.__age = age
#         else:
#             print("Invalid age")
#
#
# dog = Dog("Tommy",5,"Labrador")
# dog.set_age(-5)
#
# print(dog.get_info())
#
# print(dog._bread)

from abc import ABC, abstractmethod

class Dog(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

    def display_name(self):
        print(f"Dog name: {self.name}")


class Labrador(Dog):

    def sound(self):
        print("Labrador sound")


class Beagle(Dog):

    def sound(self):
        print("Beagle sound")


dogs = [Labrador("Tommy"),Beagle("Buddy")]

for dog in dogs:
    dog.display_name()
    dog.sound()


