import csv
import os

# Set the file path for the budget data
budget_csv = os.path.join("Resources", "hw_budget_data.csv")

# Set initial values for calculations
total_months = 0
total_profit_loss = 0
profit_losses = []
previous_profit_loss = None
greatest_increase = {"date": None, "amount": 0}
greatest_decrease = {"date": None, "amount": 0}

# Read the budget data and loop through the rows
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip header row
    header = next(csvreader)
    for row in csvreader:
        # Increment total months
        total_months += 1
        
        # Add profit/loss to running total
        total_profit_loss += int(row[1])
        
        # Calculate change in profit/loss
        if previous_profit_loss is not None:
            change = int(row[1]) - previous_profit_loss
            profit_losses.append(change)
            
            # Update greatest increase and decrease
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = row[0]
                greatest_increase["amount"] = change
            elif change < greatest_decrease["amount"]:
                greatest_decrease["date"] = row[0]
                greatest_decrease["amount"] = change
        
        # Update previous profit/loss for next iteration
        previous_profit_loss = int(row[1])
        
# Calculate average change
average_change = round(sum(profit_losses) / len(profit_losses), 2)

# Print analysis results
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

# Write analysis results to a text file
output_path = os.path.join("output", "budget_analysis.txt")
if not os.path.exists(output_path):
    with open(output_path, 'w'): pass
with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_loss}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")
