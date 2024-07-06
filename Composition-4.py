class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Гав!"


class Cat(Animal):
    def speak(self):
        return "Мяу!"


class Duck(Animal):
    def speak(self):
        return "Кря!"


def animal_sound(animal):
    return animal.speak()


dog = Dog()
cat = Cat()
duck = Duck()

print(animal_sound(dog))   # Вывод: Гав!
print(animal_sound(cat))   # Вывод: Мяу!
print(animal_sound(duck))  # Вывод: Кря!
