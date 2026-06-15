import json

class Tracker:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def delete_entry(self, index):
        if index >= 0 and index < len(self.entries):
            del self.entries[index]
            return True
        else:
            return False
    
    def total_expences(self):
        total = 0.0
        for entry in self.entries:
            if entry.category.lower() != "salary":
                total += entry.amount
        return total

    def total_balance(self):
        total = 0.0
        for entry in self.entries:
            total = total + entry.amount
        return total

    def list_by_date(self):
        sorted_entries = self.entries[:]

        for i in range(len(sorted_entries)):
            for j in range(i + 1, len(sorted_entries)):
                if sorted_entries[i].date > sorted_entries[j].date:
                    temp = sorted_entries[i]
                    sorted_entries[i] = sorted_entries[j]
                    sorted_entries[j] = temp

        return sorted_entries

    def list_by_category(self, category):
        result = []
        for entry in self.entries:
            if entry.category.lower() == category.lower():
                result.append(entry)
        return result

    def export_to_json(self, filename):
        data = {}
        index = 1

        for entry in self.entries:
            data[str(index)] = entry.to_dict()
            index = index + 1

        file = open(filename, "w")
        json.dump(data, file, indent=4)
        file.close()