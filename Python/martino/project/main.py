from tracker import Tracker
from entry import Entry
import re

DATE_PATTERN = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"

def get_valid_amount():
    while True:
        value = input("Amount : $ ")
        try:
            amount = float(value)
            if amount <= 0:
                print("Amount must be greater than zero")
            else :
                return amount
        except ValueError:
            print("Invalid number")

def valid_category(category):
    list_of_categories = ["food", "fent", "subscriptions", "transport", "salary"]
    if category.lower() in list_of_categories:
        return True
    else:
        return False
    
def valid_date(date):
    match = re.match(DATE_PATTERN, date)
    if match:
        return True
    else:
        return False
    
def main():
    tracker = Tracker()
    
    while True: 
        print("Expense Tracker Menu :")
        print("1. Add Entry")
        print("2. Delete Entry")
        print("3. View All Entries")
        print("4. View by Category")
        print("5. View Total Expense")
        print("6. View Total Balance")
        print("7. Export to JSON")
        print("8. Exit")
        
        choose = input("Choose an option : ")
        
        if choose == "1":
            amount = get_valid_amount()
            
            category = input("Category :")
            if not valid_category(category):
                print("Invalid category")
                continue
            
            date = input("Date (DD-MM-YYYY) : ")
            if not valid_date(date):
                print("Invalid date format")
                continue
            
            description = input("Description : ") 
            
            entry = Entry(amount, category, date, description)
            tracker.add_entry(entry)
            print("Entry added successfully.")
            
        elif choose == "2":
            i = 0
            for entry in tracker.entries:
                print(str(i) + ". " + str(entry))
                i += 1
            
            index_input = input("Index to delete : ")
            if index_input.isdigit():
                index = int(index_input)
                success = tracker.delete_entry(index)
                if success:
                    print("Entry deleted successfully.")
                else:
                    print("Invalid index.")
            else:
                print("Invalid input.")
                
        elif choose == "3":
            entries = tracker.list_by_date()
            for entry in entries:
                print(entry)
                
        elif choose == "4":
            category = input("Category : ")
            results = tracker.list_by_category(category)
            for entry in results:
                print(entry)
            
        elif choose == "5":
            total = tracker.total_expense()
            print("Total Expenses: $", total)
        
        elif choose == "6":
            total = tracker.total_balance()
            print("Total Balance: $", total)
            
        elif choose == "7":
            tracker.export_to_json("data.json")
            print("Data exported to data.json")
        
        elif choose == "8":
            print("Program exited.")
            break

if __name__ == "__main__":
    main()