class Fruit:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def __str__(self):
        return f"{self.name}, {self.color}, {self.weight} г"

class Basket:
    def __init__(self):
        self.fruits = []

    def add_fruit(self, fruit): 
        self.fruits.append(fruit)

    def total_weight(self):
        return sum(fruit.weight for fruit in self.fruits)

    def show_fruits(self):
        for fruit in self.fruits:
            print(fruit)

class Customer:
    def __init__(self, name):
        self.name = name
        self.basket = Basket() 

    def add_to_basket(self, fruit):
        self.basket.add_fruit(fruit)

    def show_basket(self):
        self.basket.show_fruits()

    def total_basket_weight(self):
        return self.basket.total_weight()


# Создаём клиента
alice = Customer("Alice")

# Добавляем фрукты в её корзину
alice.add_to_basket(Fruit("Яблоко", "Красное", 150))
alice.add_to_basket(Fruit("Банан", "Жёлтый", 120))

# Показать корзину и общий вес
print(f"{alice.name} корзина:")
alice.show_basket()
print("Общий вес:", alice.total_basket_weight(), "г")

# Создаём клиента
bob = Customer("Bob")

# Добавляем фрукты в его корзину
bob.add_to_basket(Fruit("Апельсин", "Оранжевый", 200))
bob.add_to_basket(Fruit("Груша", "Зелёная", 170))
bob.add_to_basket(Fruit("Яблоко", "Зелёное", 160))

# Показать корзину и общий вес
print(f"\n{bob.name} корзина:")
bob.show_basket()
print("Общий вес:", bob.total_basket_weight(), "г")


