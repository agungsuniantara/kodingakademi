class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student(Human):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def id(self):
        print(f"My student ID is {self.student_id}.")

student1 = Student("Alice", 20, "S12345")
student1.introduce()
student1.id()

positif = []
negatif = []

def banding(angka):
    if angka > 0:
        positif.append(angka)
    elif angka < 0:
        negatif.append(angka)

banding(5)