class FarmRecord:
    """Represents one crop harvest and sales record."""
 
    def __init__(self, farmer_name, crop_name, quantity_harvested,
                 expenses, sales_income):
        self.farmer_name = farmer_name
        self.crop_name = crop_name
        self.quantity_harvested = quantity_harvested
        self.expenses = expenses
        self.sales_income = sales_income
 
    def calculate_profit(self):
        """Return income minus expenses; a negative value is a loss."""
        return self.sales_income - self.expenses
 
    def display_info(self):
        """Display a readable summary of this farm record."""
        profit = self.calculate_profit()
        print("\n--- Farm Record ---")
        print(f"Farmer: {self.farmer_name}")
        print(f"Crop: {self.crop_name}")
        print(f"Quantity harvested: {self.quantity_harvested:g} units")
        print(f"Expenses: SLE {self.expenses:,.2f}")
        print(f"Sales income: SLE {self.sales_income:,.2f}")
        if profit >= 0:
            print(f"Profit: SLE {profit:,.2f}")
        else:
            print(f"Loss: SLE {abs(profit):,.2f}")
 
 
class FarmTracker:
    """Stores and manages multiple farm records."""
 
    def __init__(self):
        # Required data structure: a list of FarmRecord objects.
        self.records = []
 
    @classmethod
    def system_name(cls):
        """Class method: returns the system name."""
        return "Farm Crop Yield and Sales Tracker"
 
    def add_record(self, record):
        """Add a FarmRecord object to the list."""
        self.records.append(record)
        print("Record added successfully.")
 
    def display_records(self):
        """Display every saved record."""
        if not self.records:
            print("No farm records have been added yet.")
            return
 
        for number, record in enumerate(self.records, start=1):
            print(f"\nRecord {number}:")
            record.display_info()
 
    def show_total_profit(self):
        """Calculate the combined profit/loss across all records."""
        total = sum(record.calculate_profit() for record in self.records)
        print(f"Combined profit/loss: SLE {total:,.2f}")
 
 
def read_non_negative_number(prompt):
    """Read a number and reject invalid or negative values."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter zero or a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number, for example 12 or 12.5.")
 
 
def main():
    tracker = FarmTracker()
    print("=" * 45)
    print(FarmTracker.system_name())
    print("=" * 45)
 
    while True:
        print("\nMENU")
        print("1. Add farm record")
        print("2. Display all records")
        print("3. Show combined profit/loss")
        print("4. Exit")
 
        choice = input("Choose an option (1-4): ").strip()
 
        if choice == "1":
            farmer = input("Farmer name or nickname: ").strip()
            crop = input("Crop name (e.g., rice, cassava, groundnut): ").strip()
 
            if not farmer or not crop:
                print("Farmer name and crop name cannot be empty.")
                continue
 
            quantity = read_non_negative_number("Quantity harvested (units/bags): ")
            expenses = read_non_negative_number("Total expenses in SLE: ")
            income = read_non_negative_number("Total sales income in SLE: ")
 
            record = FarmRecord(farmer, crop, quantity, expenses, income)
            tracker.add_record(record)
 
        elif choice == "2":
            tracker.display_records()
 
        elif choice == "3":
            tracker.show_total_profit()
 
        elif choice == "4":
            print("Thank you for using the Farm Tracker. Goodbye!")
            break
 
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
 
 
if __name__ == "__main__":
    main()
