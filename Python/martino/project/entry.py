"""
This file will contain the Entry class,
make sure to test everything appropriately.
"""

class Entry:
    def __init__(self, amount, category, date, description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
    
    def __str__(self):
        return f"{self.date} | {self.category} | ${self.amount} | {self.description}"
    