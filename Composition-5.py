class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []  # Композиция: корзина содержит товары

    def add_item(self, product):
        self.items.append(product)

    def total_price(self):
        return sum(item.price for item in self.items)


class Discount:
    def apply(self, total):
        pass


class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply(self, total):
        return total * (1 - self.percentage / 100)


class FixedDiscount(Discount):
    def __init__(self, amount):
        self.amount = amount

    def apply(self, total):
        return max(0, total - self.amount)


class Order:
    def __init__(self, cart, discount):
        self.cart = cart  # Композиция: заказ содержит корзину
        self.discount = discount  # Композиция: заказ содержит скидку

    def total_price(self):
        total = self.cart.total_price()
        return self.discount.apply(total)  # Полиморфизм: применяем разные типы скидок


# Использование
cart = ShoppingCart()
cart.add_item(Product("Книга", 10))
cart.add_item(Product("Ручка", 2))

percent_discount = PercentageDiscount(10)
fixed_discount = FixedDiscount(5)

order1 = Order(cart, percent_discount)
order2 = Order(cart, fixed_discount)

print(f"Цена со скидкой 10%: {order1.total_price()}")
print(f"Цена с фиксированной скидкой $5: {order2.total_price()}")
