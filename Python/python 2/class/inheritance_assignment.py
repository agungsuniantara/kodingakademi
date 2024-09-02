class person:
    def __init__(self, nama):
        self.nama = nama

    def walk(self):
        print(f"{self.nama} sedang jalan")


class employee(person):
    def __init__(self, nama, EmployeeID):
        super().__init__(nama)
        self.id = EmployeeID

    def work(self):
        print(f"{self.nama} kerja dengan id {self.id}")


class customer(person):
    def __init__(self, nama, CustomerId):
        super().__init__(nama)
        self.id = CustomerId

    def work(self):
        print(f"{self.nama} adalah customer dengan id {self.id}")


class manager(employee):
    def __init__(self, nama, EmployeeID, jabatan):
        super().__init__(nama, EmployeeID)
        self.jabatan = jabatan

    def work_2(self):
        print(f"{self.nama} kerja dengan id {self.id} jabatan {self.jabatan}")


class developer(employee):
    def __init__(self, nama, EmployeeID, jabatan):
        super().__init__(nama, EmployeeID)
        self.jabatan = jabatan

    def work_2(self):
        print(f"{self.nama} kerja dengan id {self.id} jabatan {self.jabatan}")


alice = person("alice")
bob = employee("Bob", "0001")
rena = customer("Rena", "0002")
sam = manager("Sam", "10", "Manager")
rita = developer("Rita", "09", "Developer")

alice.walk()
bob.work()
rena.work()
sam.work_2()
rita.work_2()
