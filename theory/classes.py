class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name.upper()} barks woof woof")

dog_1 = Dog("Abd", 19)
dog_2 = Dog("Ffh", 20)
dog_1.bark()
dog_2.bark()