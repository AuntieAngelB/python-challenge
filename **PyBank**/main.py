#RBooth
#'AZPHX20190219DATA
# Unit 3| Assignment - Py Me Up, Charlie
#******************************************

# Assignment to analyize the financial records found in budget_data.csv.
# These results then must be available in terminal readout and in a textfile.

#******************************************i
# Start by importing dependencies
import os
# Import CSV module and CSV Dictionary Reader and Writer
import csv


outputfile='budget_output.txt'
from decimal import Decimal
# Create variables to report findings
profit_loss=[]
pl_summary={}

csvpath = os.path.join('budget_data.csv')
with open(csvpath) as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    next(budget_reader)
    
    total=0
    total_months=0
    # Convert budget_reader string to a list profit_loss
    for line in budget_reader:
        profit_loss.append(line)
        # The total net amount of "Profit/Losses" over the entire period
        total+=int(line[1])
        # The total number of months included in the dataset
        total_months+=1
       
    subtract_when_of_pl=0
    tot_when_of_pl=0
    Avg_when_of_pl=0
    # Initialize max increase and max decrease values with latest increase/decrease value
    max_decrease=int(profit_loss[total_months-1][1])-int(profit_loss[total_months-2][1])
    max_increase=int(profit_loss[total_months-1][1])-int(profit_loss[total_months-2][1])
    # Compute the change in "Profit/Losses" between months over the entire period
    # by iterating (backwards) from latest month-year to the earliest
    for i in range(total_months,1,-1): # stops when i is 2
        subtract_when_of_pl=int(profit_loss[i-1][1])-int(profit_loss[i-2][1])
        # Find the Greatest Increase (max_increase) and Greatest Decrease (max_decrease)
        if subtract_when_of_pl < max_decrease:
            min_month_yr=profit_loss[i-1][0]
            max_decrease=subtract_when_of_pl
        elif subtract_when_of_pl > max_increase:
            max_increase=subtract_when_of_pl
            max_month_yr=profit_loss[i-1][0]
        # Total amount change in "Profit/Losses" between months over the entire period
        tot_when_of_pl=tot_when_of_pl+subtract_when_of_pl
    #The average change in "Profit/Losses" between months over the entire period 
    tot_when_of_pl = float(tot_when_of_pl)
    total_months = float(total_months)  
    Avg_when_of_pl = (tot_when_of_pl/(total_months-1))
        

'''
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
'''
text_file=open(outputfile,"w")
# Output to text file
text_file.write('Financial Analysis')
# Output to console
print('Financial Analysis')
# Output to text file
text_file.write('\n----------------------------')
# Output to console
print('----------------------------')
# Output to text file
text_file.write('\nTotal Months: '+str(total_months))
# Output to console
print('Total Months: '+str(total_months))
# Output to text file
text_file.write('\nTotal: $'+str(total))
# Output to console
print('Total: $'+str(total))
# Output to text file
text_file.write('\nAverage Change: $'+str(round(Avg_when_of_pl,2)))
# Output to console
print('Average Change: $'+str(round(Avg_when_of_pl,2)))
# Output to text file
text_file.write('\nGreatest Increase in Profits: '+max_month_yr+' ($'+str(max_increase)+')')
# Output to console
print('Greatest Increase in Profits: '+max_month_yr+' ($'+str(max_increase)+')')
# Output to text file
text_file.write('\nGreatest Decrease in Profits: '+min_month_yr+' ($'+str(max_decrease)+')')
# Output to console
print('Greatest Decrease in Profits: '+min_month_yr+' ($'+str(max_decrease)+')')
# Close text file
text_file.close()