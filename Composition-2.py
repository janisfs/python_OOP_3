class Engine:
    def start(self):
        return "Двигатель запущен"


class Car:
    def __init__(self):
        self.engine = Engine()  # Композиция

    def start_car(self):
        return f"Автомобиль заводится: {self.engine.start()}"


my_car = Car()
print(my_car.start_car())  # Вывод: Автомобиль заводится: Двигатель запущен
