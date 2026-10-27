# Farm Crop Yield and Sales Tracker

A beginner-friendly Python Object-Oriented Programming (OOP) project that helps farmers record crop harvest quantities, farm expenses, and sales income, then calculate profit or loss.

## Features
- Add a farm record with the farmer's name or nickname and crop name.
- Record quantity harvested, expenses, and sales income in Sierra Leonean leones (SLE).
- Calculate profit or loss for each record and combined profit/loss.
- Display all records entered during the current run.
- Validate numeric inputs and reject negative values.
- Demonstrates Python classes, objects, instance methods, a class method, and a list.

## Requirements
- Python 3
- No third-party packages required.

## How to Run
1. Save the program code as `farm_tracker.py`.
2. Open a terminal or command prompt in that folder.
3. Run:

   ```bash
   python farm_tracker.py
   ```

   If your system uses `python3`, run `python3 farm_tracker.py`.
4. Follow the on-screen menu.

## Menu Options
1. **Add farm record** — enter the farmer name or nickname, crop, quantity harvested, expenses, and sales income.
2. **Display all records** — show each record and its profit or loss.
3. **Show combined profit/loss** — calculate the total result across all records.
4. **Exit** — close the program.

## Profit/Loss Calculation
`Profit or Loss = Sales Income - Expenses`

- A positive result means profit.
- A negative result means loss.
- Zero means income and expenses are equal.

Example: sales income of SLE 2,300 minus expenses of SLE 1,500 gives a profit of SLE 800.

## OOP Structure
- `FarmRecord`: represents one harvest and sales record.
- `FarmTracker`: manages a list of `FarmRecord` objects.
- `calculate_profit()`: instance method that calculates the result for one record.
- `system_name()`: class method that returns the program name.

## Data Storage and Limitations
Records are stored in a Python list in memory. **They are not saved to a file or database**, so they are lost when the program closes. This is an educational prototype, not a production farm-management system.

Possible future improvements include saving records to CSV or a database, recording dates and seasons, tracking unsold produce, and generating reports by crop.

## Digital Public Goods Considerations
- **Open source:** source code can be shared and adapted under the project's license.
- **Accessibility:** simple menu and clear prompts.
- **Privacy:** the program does not request sensitive personal information.
- **Reusability:** responsibilities are separated into classes and methods.

## License
This project is licensed under the MIT License. See the `LICENSE` file.

## Educational Use
Review and test the code, and adapt it to your assignment instructions before submission.
