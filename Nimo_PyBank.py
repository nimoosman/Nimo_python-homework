#Nimo - Python Homework - PyBank
#18 June 2019

import os
import csv


budget_data = os.path.join('..', 'Python-Homework', 'budget_data.csv')


with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    months = []
    PL = []

    for rows in csvreader:
        PL.append(int(rows[1]))
        months.append(rows[0])

    
    ProfitLosses = []

    for x in range(1, len(PL)):
        ProfitLosses.append((int(PL[x]) - int(PL[x-1])))

    print("Financial Analysis") 

    print("=====================================================")

#The average of the changes in "Profit/Losses" over the entire period
    average_change = sum(ProfitLosses) / len(ProfitLosses)
    
    total_months = len(months)

    print("total months: " + str(total_months))

    print("Total: " + "$" + str(sum(PL)))
    
    print(f"Average change: " + "$" + str(average_change))
    
#The greatest increase in profits (date and amount) over the entire period
    
    greatest_increase = max(ProfitLosses)
#The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(ProfitLosses)
  
    print("Greatest Increase in Profits: " + str(months[ProfitLosses.index(max(ProfitLosses))+1]) + " " + "$" + str(greatest_increase))

    print("Greatest Decrease in Profits: " + str(months[ProfitLosses.index(min(ProfitLosses))+1]) + " " + "$" + str(greatest_decrease))

    print("=====================================================")

#Output as txt file

PLfile = open("PyBank.txt","w")

PLfile.write("Financial Analysis")

PLfile.write("===================================================")

PLfile.write("total months: " + str(total_months))

PLfile.write("Total: " + "$" + str(sum(PL)))

PLfile.write("Average change: " + "$" + str(average_change))

PLfile.write("Greatest Increase in Profits: " + str(months[ProfitLosses.index(max(ProfitLosses))+1]) + " " + "$" + str(greatest_increase))

PLfile.write("Greatest Decrease in Profits: " + str(months[ProfitLosses.index(min(ProfitLosses))+1]) + " " + "$" + str(greatest_decrease) + "\n")

PLfile.write("===================================================" + "\n")


#End PyBank Homework 


