import os
import csv

# Defining the path where the file whose information we are going to use is stored
election_csv = os.path.join('Resources','election_data.csv')

#Total numbers of votes cast

def votes_count(csv_file):
    total_vote_count = 0
    
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        
        for row in csvreader:
            total_vote_count += 1
    
    return total_vote_count

total_votes = votes_count(election_csv)
print(f"Election Results")
print(f"-----------------------")
print(f"Total Votes: {total_votes}")

#A complete list of candidates who received votes, calculate how many votes they received, the % those votes represent
#and who was the winner of the election

def candidates_votes(csv_file):
    sum_Charles_Casper_Stockham = 0
    sum_Diana_DeGette = 0
    sum_Raymon_Anthony_Doane = 0
    Total_sum=0
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        for row in csvreader:
            if row[2]=="Charles Casper Stockham":
                sum_Charles_Casper_Stockham+=1
            elif row[2]=="Diana DeGette":
                sum_Diana_DeGette+=1
            else:
                sum_Raymon_Anthony_Doane+=1
    Total_sum=sum_Charles_Casper_Stockham + sum_Diana_DeGette + sum_Raymon_Anthony_Doane
    percentage_charles=round((sum_Charles_Casper_Stockham/Total_sum)*100,3)
    percentage_diana=round((sum_Diana_DeGette/Total_sum)*100,3)
    percentage_raymon=round((sum_Raymon_Anthony_Doane/Total_sum)*100,3)

    if sum_Charles_Casper_Stockham>sum_Diana_DeGette and sum_Charles_Casper_Stockham>sum_Raymon_Anthony_Doane:
        winner="Charles Casper Stockham"
    elif sum_Diana_DeGette>sum_Charles_Casper_Stockham and sum_Diana_DeGette > sum_Raymon_Anthony_Doane:
        winner="Diana DeGette"
    elif sum_Raymon_Anthony_Doane>sum_Charles_Casper_Stockham and sum_Raymon_Anthony_Doane > sum_Diana_DeGette:
        winner="Raymon Anthony Doane"

    return sum_Charles_Casper_Stockham, sum_Diana_DeGette, sum_Raymon_Anthony_Doane, percentage_charles, percentage_diana, percentage_raymon, winner



sum_Charles_Casper_Stockham, sum_Diana_DeGette, sum_Raymon_Anthony_Doane, percentage_charles, percentage_diana, percentage_raymon, winner=candidates_votes(election_csv)
print(f"Charles Casper Stockham:{percentage_charles}% ({sum_Charles_Casper_Stockham})")
print(f"Diana DeGette:{percentage_diana}% ({sum_Diana_DeGette})")
print(f"Raymon Anthony Doane:{percentage_raymon}% ({sum_Raymon_Anthony_Doane})")
print(f"-----------------------------------")
print(f"Winner: {winner}")

#Exporting the information to a text file
output_path = os.path.join('Analysis','analysis.txt')
with open(output_path, 'w') as file:
    file.write(f"Election Results\n")
    file.write(f"-----------------------\n")
    file.write(f"Total Votes {total_votes}\n")
    file.write(f"-----------------------\n")
    file.write(f"Charles Casper Stockham: {percentage_charles}% ({sum_Charles_Casper_Stockham})\n")
    file.write(f"Diana DeGette: {percentage_diana}% ({sum_Diana_DeGette})\n")
    file.write(f"Raymon Anthony Doane: {percentage_raymon}% ({sum_Raymon_Anthony_Doane})\n")
    file.write(f"-----------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write(f"-----------------------\n")
    
