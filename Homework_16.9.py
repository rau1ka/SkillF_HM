# Задание 16.9.1 и 16.9.2
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"Rectangle: {self.x}, {self.y}, {self.width}, {self.height}"

    def get_area(self):
        return self.width * self.height
    
rect_1 = Rectangle(5,10,50,100)
print(rect_1)
print(rect_1.get_area())

# Задание 16.9.3 и 16.9.4
class Client:
    def __init__(self, name, female, city, balance):
        self.name = name
        self.female = female
        self.city = city
        self.balance = balance

    def __str__(self):
        return f"{self.name} {self.female}. {self.city}. Баланс: {self.balance}руб."

    def big_party(self):
        return f"{self.name} {self.female}. {self.city}."

client_1 = Client('Иван', 'Петров', 'Москва', 50)
client_2 = Client('Люда', 'Соколова', 'Казань', 60)
client_3 = Client('Витя', 'Тараканов', 'Челябинск', 45)

client_list = [client_1, client_2, client_3]

for guests in client_list:
    print(guests.big_party())

print(client_1)

