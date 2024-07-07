class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def eat(self):
        print(f"{self.name} ест.")


class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} чирикает.")


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит.")


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} шипит.")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            print("Не верный вид животного")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def show_all_animals(self):
        for animal in self.animals:
            print(f"{animal.name}, {animal.age} лет")

    def show_all_staff(self):
        for staff_member in self.staff:
            print(f"{staff_member.name}, {staff_member.role}")


class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class ZooKeeper(Staff):
    def __init__(self, name):
        super().__init__(name, "работник зоопарка")

    def feed_animal(self, animal):
        if isinstance(animal, Animal):
            print(f"{self.name} кормит {animal.name}")
        else:
            print("Не верный вид животного")


class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name, "Ветеринар")

    def heal_animal(self, animal):
        if isinstance(animal, Animal):
            print(f"{self.name} лечит {animal.name}")
        else:
            print("Не верный вид животного")


# Пример использования классов
# Создание экземпляров животных
bird = Bird("Попугай", 2, 25)
mammal = Mammal("Лев", 5, "Golden")
reptile = Reptile("Змея", 3, "Scales")

# Создание зоопарка
zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

# Создание сотрудников
keeper = ZooKeeper("Иван")
vet = Veterinarian("Алиса")
zoo.add_staff(keeper)
zoo.add_staff(vet)

# Вывод информации о животных и сотрудниках
zoo.show_all_animals()
zoo.show_all_staff()

# Демонстрация полиморфизма
animals = [bird, mammal, reptile]
animal_sound(animals)

# Сотрудники выполняют свои действия
keeper.feed_animal(mammal)
vet.heal_animal(reptile)
