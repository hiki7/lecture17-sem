class Animal:
    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs

    def voice(self):
        print(f"{self.name} подает голос")

    def move(self):
        print(f"{self.name} дергает хвостом")


class Dog(Animal):
    def __init__(self, name, species, legs, breed=None):
        super().__init__(name, species, legs)
        self.breed = breed

    @classmethod
    def with_breed(cls, name, species, legs, breed):
        return cls(name, species, legs, breed)

    @classmethod
    def without_breed(cls, name, species, legs):
        return cls(name, species, legs)

    def bark(self):
        print(f"{self.species} {self.name} лает")


class Bird(Animal):
    def __init__(self, name, species, legs, wingspan=None):
        super().__init__(name, species, legs)
        self.wingspan = wingspan

    @classmethod
    def with_wingspan(cls, name, species, legs, wingspan):
        return cls(name, species, legs, wingspan)

    @classmethod
    def without_wingspan(cls, name, species, legs):
        return cls(name, species, legs)

    def fly(self):
        print(f"{self.species} {self.name} летaeт")


dog = Dog("Геральт", "доберман", 4)
bird = Bird("Вася", "попугай", 2)
dog.voice()
bird.voice()
dog.move()
bird.move()
dog.bark()
bird.fly()