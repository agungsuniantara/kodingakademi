class employee:
    def __init__(self):
        self.dict = {} 
    
    def add_employee(self, name, age, salary):
        self.dict[name] = {"age": age, "salary": salary}
    
    def search_employee(self, name):
        if name in self.dict:
            return self.dict[name]
        else:
            return "Employee not found"
        
    def update_employee(self, name, age, salary):
        if name in self.dict:
            self.dict[name]["age"] = age
            self.dict[name]["salary"] = salary
        else:
            return "Employee not found"
        
    def delete_employee(self, name):
        if name in self.dict:
            del self.dict[name]
        else:
            return "Employee not found"

while True:
    print("1. Add Employee")
    print("2. Search Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        salary = int(input("Enter salary: "))
        employee.add_employee(name, age, salary)
    elif choice == 2:
        name = input("Enter name: ")
        print(employee.search_employee(name))
    elif choice == 3:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        salary = int(input("Enter salary: "))
        employee.update_employee(name, age, salary)
    elif choice == 4:
        name = input("Enter name: ")
        employee.delete_employee(name)
    elif choice == 5:
        break
    else:
        print("Invalid choice")