import os
import csv

# Defining the path where the file whose information we are going to use is stored
budget_csv = os.path.join('C:/Users/diego/Python-Challenge/PyBank','Resources','budget_data.csv')

#Calculating the total number of months included in the dataset

def months_count(csv_file):
    total_month_count = 0
    
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        
        for row in csvreader:
            total_month_count += 1
    
    return total_month_count

total_months = months_count(budget_csv)
print(f"Financial Analysis")
print(f"-----------------------")
print(f"Total Months: {total_months}")

#The net total amount of "Profit/Losses" over the entire period

def profit_losses(csv_file):
    total_net_amount = 0
    
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        
        for row in csvreader:
            profit_losses = int(row[1])
            total_net_amount += profit_losses
    
    return total_net_amount

total_amount = profit_losses(budget_csv)
print(f"Total: ${total_amount}")

#The changes in "Profit/Losses" over the entire period, and then the average of those changes. Additionally, in this section
# the greatest increase in profits and the greatest decrease in profits are calculated (Date and amount)
def changes_profit_losses(csv_file):
    total_changes_profit_losses = 0
    total_months = 0
    changes_list = []
    dates_list=[]
 

    with open(csv_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)

        previous_profit_losses = 0

        for row in csvreader:
            dates_list.append(str(row[0]))
            profit_losses = int(row[1])
            if total_months > 0:
                change = profit_losses - previous_profit_losses
                total_changes_profit_losses += change
                changes_list.append(change)
            previous_profit_losses = profit_losses
            total_months += 1

    average_change = round(total_changes_profit_losses / (total_months - 1), 2)
    max_index = changes_list.index(max(changes_list))
    min_index = changes_list.index(min(changes_list))
    greatest_increase_date = dates_list[max_index+1]
    greatest_decrease_date = dates_list[min_index+1]

    return total_changes_profit_losses, average_change, changes_list, dates_list, greatest_decrease_date, greatest_increase_date

total_changes, average_change, changes_list, dates_list, greatest_decrease_date, greatest_increase_date= changes_profit_losses(budget_csv)

print(f"Average Change: ${average_change}")
print(f"Greatest Increase in profits: {greatest_increase_date} (${max(changes_list)})")
print(f"Greatest Decrease in profits: {greatest_decrease_date} (${min(changes_list)})")

#Exporting the information to a text file
output_path = os.path.join('C:/Users/diego/Python-Challenge/PyBank', "Analysis", "analysis.txt")
with open(output_path, 'w') as file:
    file.write(f"Financial Analysis\n")
    file.write(f"-----------------------\n")
    file.write(f"Total Months {total_months}\n")
    file.write(f"Total ${total_amount}\n")
    file.write(f"Average Change ${average_change}\n")
    file.write(f"Greatest Increase in profits {greatest_increase_date} ${max(changes_list)}\n")
    file.write(f"Greatest Decrease in profits {greatest_decrease_date} ${min(changes_list)}\n")
