class Dog:

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog name: {self.name}")


class Labrador(Dog):

    def sound(self):
        print("Labrador sound")


class GuideDog(Labrador):
    def guide(self):
        print(f"{self.name}guides the way")


class Friendly:

    def greet(self):
        print("Friendly dog")


class GolderRetriever(Dog,Friendly):

    def sound(self):
        print("Golder Retriever sound")


lab = Labrador("Buddy")
lab.display_name()
lab.sound()

guide_dog = GuideDog("Tommy")
guide_dog.display_name()
guide_dog.sound()
guide_dog.guide()

retriever = GolderRetriever("Max")
retriever.display_name()
retriever.sound()
retriever.greet()