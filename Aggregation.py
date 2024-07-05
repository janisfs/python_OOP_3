class Teacher():
    def teach(self):
        print("Преподаватель учит")

class School():
    def __init__(self, new_teacher):
        self.teacher = new_teacher

    def start_lesson(self):
        self.teacher.teach()

my_teacher = Teacher()  # Учитель создается отдельно
my_school = School(my_teacher)  # Учитель передается в школу
my_school.start_lesson()  # Вызывает метод учителя через школу
