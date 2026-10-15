class student:
    def __init__(self):
        self.data = {}
    
    def add(self, name, id, age, major, address):
        self.data[id] = [name, age, major, address]
    
    def show(self):
        for key, value in self.data.items():
            print(f"id : {key}")
            print(f"Name : {value[0]}")
            print(f"age : {value[1]}")
            print(f"major : {value[2]}")
            print(f"address : {value[3]}")
    
    def edit(self, id):
        for key, value in self.data.items():
            if key == id:
                value[0] = input("insert new name : ")
                value[1] = input("insert new age : ")
                value[2] = input("insert new major : ")
                value[3] = input("insert new address : ")
    
    def delete(self, id):
        if id in self.data:
            del self.data[id]

database = student()
database.add("agung", "101010", "20 years old", "computer science", "canggu")
database.add("ziya", "555", "25 years old", "computer science", "canggu")
database.show()

# database.edit("101010")
# database.show()

database.delete("101010")
database.show()



        