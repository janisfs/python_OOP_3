class Engine:
    def start(self):
        return "Обычный двигатель запущен"


class ElectricEngine(Engine):
    def start(self):
        return "Электрический двигатель запущен"


class Car:
    def __init__(self, engine):
        self.engine = engine  # Композиция

    def start_car(self):
        return f"Автомобиль заводится: {self.engine.start()}"


normal_car = Car(Engine())
electric_car = Car(ElectricEngine())

print(normal_car.start_car())   # Вывод: Автомобиль заводится: Обычный двигатель запущен
print(electric_car.start_car())  # Вывод: Автомобиль заводится: Электрический двигатель запущен
