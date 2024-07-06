class Notification:
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print(f"Отправка email: {message}")


class SMSNotification(Notification):
    def send(self, message):
        print(f"Отправка SMS: {message}")


class PushNotification(Notification):
    def send(self, message):
        print(f"Отправка Push-уведомления: {message}")


class User:
    def __init__(self, name, notification_preference):
        self.name = name
        self.notification = notification_preference  # Композиция

    def notify(self, message):
        self.notification.send(f"Привет, {self.name}! {message}")  # Полиморфизм


# Использование
email_user = User("Алиса", EmailNotification())
sms_user = User("Боб", SMSNotification())
push_user = User("Чарли", PushNotification())

users = [email_user, sms_user, push_user]

for user in users:
    user.notify("У нас новые акции!")  # Полиморфизм в действии
