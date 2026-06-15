import re
from tracker import Tracker
from entry import Entry

DATE_PATTERN = r"^\d{4}-\d{2}-\d{2}$"
CATEGORY_PATTERN = r"^[A-Za-z]+$"

def valid_date(date):
    match = re.match(DATE_PATTERN, date)
    if match:
        return True
    else:
        return False

def valid_category(category):
    match = re.match(CATEGORY_PATTERN, category)
    if match:
        return True
    else:
        return False

def get_valid_amount():
    while True:
        value = input("Amount: ")
        try:
            amount = float(value)
            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                return amount
        except ValueError:
            print("Invalid number.")


def main():
    tracker = Tracker()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Entry")
        print("2. Delete Entry")
        print("3. View All Entries")
        print("4. View by Category")
        print("5. View Total Expense")
        print("6. Export to JSON")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = get_valid_amount()

            category = input("Category: ")
            if not valid_category(category):
                print("Invalid category.")
                continue

            date = input("Date (YYYY-MM-DD): ")
            if not valid_date(date):
                print("Invalid date format.")
                continue

            description = input("Description (optional): ")

            entry = Entry(amount, category, date, description)
            tracker.add_entry(entry)
            print("Entry added successfully.")

        elif choice == "2":
            i = 0
            for entry in tracker.entries:
                print(str(i) + ". " + str(entry))
                i += 1

            index_input = input("Index to delete: ")
            if index_input.isdigit():
                index = int(index_input)
                success = tracker.delete_entry(index)
                if success:
                    print("Entry deleted.")
                else:
                    print("Invalid index.")
            else:
                print("Invalid input.")

        elif choice == "3":
            entries = tracker.list_by_date()
            for entry in entries:
                print(entry)

        elif choice == "4":
            category = input("Category: ")
            results = tracker.list_by_category(category)

            if len(results) == 0:
                print("No entries found.")
            else:
                for entry in results:
                    print(entry)
                    
        elif choice == "5":
            total = tracker.total_expense()
            print("Total Expense:", total)

        elif choice == "6":
            total = tracker.total_balance()
            print("Total Balance:", total)

        elif choice == "7":
            tracker.export_to_json("data.json")
            print("Data exported to data.json")

        elif choice == "8":
            print("Program exited.")
            break

        else:
            print("Invalid menu option.")


if __name__ == "__main__":
    main()