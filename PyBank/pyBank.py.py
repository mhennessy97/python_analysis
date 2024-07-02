#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import CSV & OS
import csv
import os

#load in CSV file for analysis

csvfile = os.path.join(".", "Resources", "budget_data.csv")

txtfile = os.path.join(".", "Resources", "budget_analysis.txt")

# file needs somewhere to begin counting months. add in value to begin counting from

totalMonths = 0

#file needs somewhere to begin counting total Profit & Losses. add in value to summarize beginning at 0

totalNet = 0

#create lists to determine averge changes in PnL for the period (netChangeList), the month associated with the greatest increase/decrease (monthOfChange), and the greatest increase or decrease. Include range in list for increase & decrease to provide values to search through. Use 0-99999999999... to make a range from 0 to an unreachable # within the dataset. 
netChangeList = []
monthOfChange = []
increase = [" ", 0]
decrease = [" ", 9999999999999999999]

# read the CSV file and convert it to a list
with open(csvfile) as financial_data:
    csvreader = csv.reader(financial_data)

   # determine the header within the dataset 
    header = next(csvreader)

    #add additional next skip the header and go to the first row to begin calculations

    firstRow = next(csvreader)

    #add in formula to skip date and pull total net PnL from column B. will need to specify as integer as well to avoid errors when calculating total sum
    totalNet += int(firstRow[1])
    previousNet = int(firstRow[1])

    totalMonths += 1
    
    # determine the total # of months included in the dataset

    for rows in csvreader: #loop through each row in the file

        totalMonths += 1 #count each row to determine the # of months included in the dataset
        
    #determine the net total amount of Profit/Losses for the entire period
        
        totalNet += int(rows[1])

    #determine average change 
        avgChange = int(rows[1]) - previousNet
        previousNet = int(rows[1])
        netChangeList.append(avgChange)

    #caluclate the gratest increase in profits
        if (avgChange > increase[1]):
            increase[0] = rows[0] 
            increase[1] = avgChange

    #calculate the greatest decrease in profits
        if (avgChange < decrease[1]):
            decrease[0] = rows[0]
            decrease[1] = avgChange

        
#create variable to get average of monthly changes. sum the net change list and divide it by the length of #s in the list. Make sure to round to 2 decimal places for $ value. 
netMonthlyAvg = round(sum(netChangeList) / len(netChangeList),2)

#print out the solutuions requested in the dataset
solution = (
    f'Financial Analysis\n'
    f'-----------------------------\n'
    f'Total Months: {totalMonths}\n'
    f'Total: ${totalNet}\n'
    f'Average Change: ${netMonthlyAvg}\n'
    f'Greatest Increase in Profits: {increase[0]} (${increase[1]})\n'
    f'Greatest Decrease in Profist: {decrease[0]} (${decrease[1]})'
)

print(solution)

#Output and create a text file with solutions
with open(txtfile, "w") as txt_file:
    txt_file.write(solution)


# In[ ]:




