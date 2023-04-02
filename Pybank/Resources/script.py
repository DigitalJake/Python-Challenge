import csv
import os

Budget_data = "Pybank/Resources/budget_data.csv"

with open(Budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csvheader = next(csvreader)
    firstline= next(csvreader)
    current_changes = 0
    months= 1
    average_changes= 0
    current_pl = 0
    total_changes= 0 
    pl_total = int(firstline[1])
    previous_pl = int(firstline[1])
    changes_list= 0
    greatest_increase = 0
    greatest_decrease= 0
    for row in csvreader:
        months +=1
        current_pl = int(row[1])
        pl_total = pl_total+ current_pl
        current_changes = current_pl - previous_pl
        previous_pl= current_pl
        total_changes = total_changes + current_changes
        average_changes = total_changes/(months -1)
        #if the current pl > than previous pl then save it and call it greatest pl
        if current_changes > greatest_increase:
            greatest_increase = current_changes
            month = row[0]
        if current_changes < greatest_decrease:
            greatest_decrease = current_changes
            month = row[0]
    # print("Financial Analysis")
    # print("----------------------------")
    # print(f"Total Months:  {months}")
    # print(f"Total:  ${pl_total}")
    # print(f"Average Change:  ${average_changes}")
    # print(f"Greatest Increase in Profits: (${greatest_increase})")
    # print(f"Greatest Decrease in Losses:  (${greatest_decrease})")
    output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {months}\n"
    f"Total: ${pl_total}\n"
    f"Average Change: ${average_changes:.2f}\n"
    f"Greatest Increase in Profits:  (${greatest_increase})\n"
    f"Greatest Decrease in Profits:  (${greatest_decrease})\n")

    print(output)
# Export the results to text file
file_to_output="Analysis/budget_analysis.txt"
with open(file_to_output, "w") as txt_file:    
    txt_file.write(output)