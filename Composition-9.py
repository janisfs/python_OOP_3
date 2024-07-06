# Создайте класс Author и класс Book. Класс Book должен использовать композицию для включения автора в
# качестве объекта.

class Author:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author  # Композиция автора в книге

    def __str__(self):
        return f"{self.title} by {self.author}"


# Создаем экземпляр класса Author
author = Author("John Doe", "john@example.com")

# Создаем экземпляр класса Book с использованием композиции автора
book = Book("A Great Novel", author)

# Выводим информацию о книге
print(book)
