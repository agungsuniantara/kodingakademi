class product:

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class buy:

    def __init__(self, day, date):
        self.day = day
        self.date = date
        self.list = []

    def history(self, items):
        self.list.append(items)

data1 = product("pen", 20, 10000)
data2 = buy("senin", "10 januari 2024")

print(data2.history(data1))
print(data2.list[0] == data1)