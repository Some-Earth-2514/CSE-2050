class Animal:
    """Parent class"""
    def __init__(self, name):
        """initializes the variable 'name'"""
        self.name = name

    def speak(self):
        """Returns a string of name and its noise"""
        return f"{self.name} says noise!"

    def reply(self):
        """Returns the function speak() """
        return self.speak()


class Mammal(Animal):
    """Child class of the Animal parent class"""
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        """Returns a string of name and its noise
        Overrides the Animal class' speak() function"""
        return f"{self.name} says mammal noises!"


class Cat(Mammal):
    """Child class of the Mammal parent class"""
    def speak(self):
        """Returns a string of name and its noise
        Overrides the Mammal class' speak() function"""
        return f'{self.name} says Meow!'


class Dog(Mammal):
    """Child class of the Mammal parent class"""
    def speak(self):
        """Returns a string of name and its noise
        Overrides the Mammal class' speak() function"""
        return f'{self.name} says Bark!'


class Primate(Mammal):
    """Child class of the Mammal parent class"""
    def speak(self):
        """Returns a string of name and its noise
        Overrides the Mammal class' speak() function"""
        return f'{self.name}says hello!'


class ComputerScientist(Primate):
    """Child class of the Primate parent class"""
    pass
