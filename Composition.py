class Teacher():
    def teach(self):
        print("Преподаватель учит")


class School():
    def __init__(self):
        self.teacher = Teacher()  # Создание учителя внутри школы

    def start_lesson(self):
        self.teacher.teach()
        

my_school = School()  # Учитель создается автоматически при создании школы
my_school.start_lesson()  # Вызывает метод учителя через школу
