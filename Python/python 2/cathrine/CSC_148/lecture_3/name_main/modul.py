def my_function():
    print("Hello from my_function!")

def add_numbers(a, b):
    return a + b

# Ini akan dijalankan jika modul.py dijalankan langsung
if __name__ == '__main__':
    print("This is executed only if modul.py is run directly.")
    result = add_numbers(3, 5)
    print("Result of addition:", result)
