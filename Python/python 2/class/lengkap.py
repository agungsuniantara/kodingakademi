class Animal:
    def __init__(self, name):
        self.__name = name  # Encapsulation: private variable

    def get_name(self):
        return self.__name

    def speak(self):
        return "Animal speaks."


class Dog(Animal):
    def speak(self):
        return f"{self.get_name()} says Woof!"  # Polymorphism


class Cat(Animal):
    def speak(self):
        return f"{self.get_name()} says Meow!"  # Polymorphism


# Penggunaan inheritance, polymorphism, dan encapsulation
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
