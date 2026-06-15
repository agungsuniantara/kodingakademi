import json

class Tracker:
    def __init__(self):
        self.entries = [] #[ Entry(amount, category, date, description), ...]
        
    def add_entry(self, entry):
        self.entries.append(entry)
        
    def delete_entry(self, index):
        if index >= 0 and index < len(self.entries):
            del self.entries[index]
            return True
        else:
            return False
    
    def list_by_date(self):
        sorted_entries = self.entries[:] 
        
        for i in range(len(sorted_entries)): # i = 0, len(sorted_entries) = 2
            for j in range(i + 1, len(sorted_entries)): # j = 1, len(sorted_entries) = 2
                if sorted_entries[i].date > sorted_entries[j].date:
                    temp = sorted_entries[i]
                    sorted_entries[i] = sorted_entries[j]
                    sorted_entries[j] = temp
        
        return sorted_entries
    
    def list_by_category(self, category):
        results = []
        for entry in self.entries:
            if entry.category.lower() == category.lower():
                results.append(entry)
        return results

    def total_expense(self):
        total = 0.0
        for entry in self.entries:
            if entry.category.lower() != "salary":
                total += entry.amount
        return total
    
    def total_balance(self):
        total = 0.0
        for entry in self.entries:
            if entry.category.lower() == "salary":
                total += entry.amount
            else:
                total -= entry.amount
        return total

    def export_to_json(self, filename):
        data = {}
        index = 1 
        
        for entry in self.entries:
            if entry.category.lower() == "salary":
                data[str(index)] = {
                    "amount": f"+{entry.amount}",
                    "category": entry.category,
                    "date": entry.date,
                    "description": entry.description
                }
            else:
                data[str(index)] = {
                    "amount": f"-{entry.amount}",
                    "category": entry.category,
                    "date": entry.date,
                    "description": entry.description
                }
            index += 1
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        
        