# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 17:18:00 2022

@author: Asus
"""

# import libraries

import os
import csv

# Set the path for the CSV file 

PyBank = os.path.join("budget_data.csv")

# lists for store data

profit = []
monthly_changes = []
date = []

# variables
 
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

# Open file

with open(PyBank, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # for loop
    for row in csvreader:    
      # Use count to count the number months in this dataset
      count = count + 1 

      # for the greatest increase and decrease 
      date.append(row[0])

      # calculate the total profit
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      # average change in profits 
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit

      # changes in a list
      monthly_changes.append(monthly_change_profits)

      total_change_profits = total_change_profits + monthly_change_profits
      initial_profit = final_profit

      # average change in profits
      average_change_profits = (total_change_profits/count)
      
      # max and min change in profits 
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
      
      #print statements, next print them in the file also
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")
