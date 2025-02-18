class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __pow__(self, power):
        return Number(self.value ** power)

    def __floordiv__(self, other):
        return Number(self.value // other.value)

    def __truediv__(self, other):
        if other.value == 0:
            return Number(0)  # Menghindari pembagian dengan nol
        return Number(self.value / other.value)

    def __neg__(self):
        return Number(-self.value)

    def __abs__(self):
        return Number(abs(self.value))

    def __invert__(self):
        return Number(~int(self.value))  # Menggunakan ~ hanya untuk tipe int

    def __repr__(self):
        return f"Number({self.value})"


# Contoh Penggunaan
num1 = Number(10)
num2 = Number(3)

print("Addition:", num1 + num2)           # __add__
print("Subtraction:", num1 - num2)        # __sub__
print("Multiplication:", num1 * num2)     # __mul__
print("Power:", num1 ** 2)                # __pow__
print("Floor Division:", num1 // num2)    # __floordiv__
print("True Division:", num1 / num2)      # __truediv__
print("Negation:", -num1)                 # __neg__
print("Absolute:", abs(Number(-10)))      # __abs__
print("Inversion:", ~Number(2))           # __invert__
