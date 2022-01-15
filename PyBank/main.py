import os
import csv

#point to file, one folder up
budget = os.path.join("Resources", "budget_data.csv")

#name variables to be used below to store 
months = []
monthtotal = []
monthly_changes = []
track_changes = []

#establish data values at 0 to begin calculations
grandtotal = 0
total_changes = 0
monthly_avg = 0
greatest_increase = 0
greatest_decrease = 0

# Open and read csv be sure you have correct delimiter
with open(budget, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    
    #set the initial value for last month- (will be overwritten in the loop)
    last_month = int(next(csv_reader)[1])
    # Read through each row of data after the header
    for row in csv_reader:
        #Count the number of months by counting the number in the list using len
        months.append(row[0])
        monthsall = len(months)
      
        #calculate the total of all P/L by adding (row 1) to grand total on each loop
        grandtotal = int(grandtotal) + int(row[1])
        
        #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        #to do this you need to find montly_changes 
        monthly_changes= int(row[1]) - int(last_month)
        #add to the total changes
        total_changes = int(total_changes) + int(monthly_changes)
        #(store these values in a new list since they will be needed again)
        track_changes.append(monthly_changes)
        #set new value for last month so when the loop moves down its accessing the correect "last month" 
        last_month = int(row[1])

        #to find average divide total change by number of months
        monthly_avg = round(int(total_changes) / int(monthsall), 2)
        
        #Find greatest increase and greatest decrease by accessing max and min in list of monthly_changes
        greatest_increase = max(track_changes)
        greatest_decrease = min(track_changes)
        #Did not find associated months- because I chose to make a new list, could not figure out how to associate my "new list" to the "old" one
        #I'm sure its something simple, but I'm at a loss. Probably should have built a dictionary to start with. 

print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {monthsall}") 
print(f"Total: ${grandtotal}")
print(f"Average Change: ${monthly_avg}")
print(f"Greatest Increase in Profits: month_increase $({greatest_increase})")
print(f"Greatest Decrease in Profits: month_decrease $({greatest_decrease})")

# Specify the path and name of file to write
output_path = os.path.join("Analysis", "bank_results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    #write headers
    writer.writerow(["Total Months", "Total", "Average Change", "Greatest Increase Profits (Month)", "Greatest Increase Profits (Total)", 
    "Greatest Decrease Profits (Month)", "Greatest Increase Profits (Total)"])
    #write results
    writer.writerow([monthsall, grandtotal, monthly_avg, "month_increase", greatest_increase, "month_decrease", greatest_decrease])