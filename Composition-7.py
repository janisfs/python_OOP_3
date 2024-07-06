# Создайте класс Animal с методом make_sound(). Затем создайте несколько дочерних классов
# (например, Dog, Cat, Cow), которые наследуют Animal, но изменяют его поведение
# (метод make_sound()). В конце создайте список содержащий экземпляры этих животных и
# вызовите make_sound()
# для каждого животного в цикле.

class Animal:
    def make_sound(self):
        print("Животное издает звук")


class Dog(Animal):
    def make_sound(self):
        print("Гав-гав!")


class Cat(Animal):
    def make_sound(self):
        print("Мяу-мяу!")


class Cow(Animal):
    def make_sound(self):
        print("Му-у-у!")


# Создаем список животных
animals = [Dog(), Cat(), Cow(), Dog(), Cat()]

# Вызываем make_sound() для каждого животного в цикле
for animal in animals:
    (animal.make_sound())


