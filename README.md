# Python-Challenge
Pybank assignment

Lines 5-21

This specific structure of how to create a function that goes through all the rows of a csv file and gives as a result one total value was provided by 
the Xpert Learning Assistant

budget_csv = os.path.join('C:/Users/diego/Python-Challenge/PyBank','Resources','budget_data.csv')

"def months_count(csv_file):
    total_month_count = 0
    
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        
        for row in csvreader:
            total_month_count += 1
    
    return total_month_count

total_months = months_count(budget_csv)"

That specific structure was used again to create functions for the net total amount of "Profit/Losses" over the entire period, the changes in "Profit/Losses" over the entire period, the average of those changes, the greatest increase in profits and the greatest decrease in profits (With dates and amounts)

Lines 84-92

This specific code ("File.write") for exporting my results to a txtfile was provided by the Xpert Learning Assistant

output_path = os.path.join('C:/Users/diego/Python-Challenge/PyBank', "Analysis", "analysis.txt")
with open(output_path, 'w') as file:
    file.write(f"Financial Analysis\n")
    file.write(f"-----------------------\n")
    file.write(f"Total Months {total_months}\n")
    file.write(f"Total ${total_amount}\n")
    file.write(f"Average Change ${average_change}\n")
    file.write(f"Greatest Increase in profits {greatest_increase_date} ${max(changes_list)}\n")
    file.write(f"Greatest Decrease in profits {greatest_decrease_date} ${min(changes_list)}\n")

PyPoll assignment

The structure of how to create functions provided by the Xpert Learning Assistant ,described in the Pybank exercise, was also used to create all the functions in the PyPoll assignment 

The structure of how to export my results to a txtfile provided by the Xpert Learning Assistant, described above in the Pybank exercise, was also used in the PyPoll assignment