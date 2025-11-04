class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def is_available(self):
        return self.quantity > 0

    def __str__(self):
        return f"Название: {self.name}, цена: {self.price}, остаток: {self.quantity}"


class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"Товар: {self.product.name}, кол-во: {self.quantity}, сумма: {self.get_total()}"


class Order:
    def __init__(self, customer):
        self.items = []
        self.customer = customer

    def add_item(self, product, quantity):
        item = OrderItem(product, quantity)
        self.items.append(item)

    def remove_item(self, product_name):
        for item in self.items:
            if item.product.name == product_name:
                self.items.remove(item)
                return "Успешно удалено"
        return "Товар не найден"

    def get_total(self):
        return sum(item.get_total() for item in self.items)

    def __str__(self):
        order_str = f"Заказ для: {self.customer}\n"
        for item in self.items:
            order_str += str(item) + "\n"
        order_str += f"Общая сумма: {self.get_total()}"
        return order_str


class Store:
    def __init__(self):
        self.products = []
        self.orders = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        for product in self.products:
            print(product)

    def find_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    def create_order(self, customer_name):
        order = Order(customer_name)
        self.orders.append(order)
        return order

    def show_orders(self):
        for order in self.orders:
            print(order)
            print("-" * 30)


# Создаём магазин
store = Store()

# Добавляем товары
bread = Product("Хлеб", 50, 10)
milk = Product("Молоко", 80, 5)
store.add_product(bread)
store.add_product(milk)

# Создаём заказ
order1 = store.create_order("Алиса")
order1.add_item(bread, 2)  # 2 хлеба
order1.add_item(milk, 1)   # 1 молоко

# Выводим товары магазина
print("Товары в магазине:")
store.show_products()
print("\nЗаказы:")
store.show_orders()
