import csv

# Read the budget data from CSV file
def read_budget_data(file_path):
    budget_data = []
    with open(file_path, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader)  # Skip the header row
        for row in reader:
            budget_data.append(row)
    return budget_data

# Perform financial analysis on the budget data
def analyse_budget_data(budget_data):
    total_months = len(budget_data)
    net_total = 0
    changes = []
    greatest_increase = {"date": "", "amount": 0}
    greatest_decrease = {"date": "", "amount": 0}

    for i in range(total_months):
        date = budget_data[i][0]
        profit_loss = int(budget_data[i][1])
        net_total += profit_loss

        if i > 0:
            change = profit_loss - int(budget_data[i-1][1])
            changes.append(change)

            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change

            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

    average_change = sum(changes) / len(changes)

    analysis_results = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase["date"]} (${greatest_increase["amount"]})
Greatest Decrease in Profits: {greatest_decrease["date"]} (${greatest_decrease["amount"]})
"""

    return analysis_results

# Write analysis results to a text file
def write_analysis_results(file_path, analysis_results):
    with open(file_path, "w") as txt_file:
        txt_file.write(analysis_results)

# Main function
def main():
    file_path = "budget_data.csv"
    output_file = "financial_analysis.txt"

    # Read budget data
    budget_data = read_budget_data(file_path)

    # Perform analysis on budget data
    analysis_results = analyse_budget_data(budget_data)

    # Print analysis results to the terminal
    print(analysis_results)

    # Write analysis results to a text file
    write_analysis_results(output_file, analysis_results)

# Run the program
if __name__ == "__main__":
    main()



