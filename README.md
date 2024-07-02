# python_analysis
README - pyBank
  Included imports for OS and CSV to pull the information from the file. 
  
  Referenced both the CSV file path and Txt file path using os.path.join
  
  Next, made sure to add in values for both totalMonths and totalNet so formulas later on knew where to begin counting
  
  Created lists for each term referenced later on in formulas. NetChangeList = the average changes for PNL for the period. Increase & Decrease entered to set a range from 0 to a # higher than any in the dataset. This sets a range to search for each value. Made sure the range was higher than the data set so no values will be missed. 

  Set formula to read the CSVfile and convert it to a list

  Needed to determine where the header is and skip past by using "next" function

  Added in formula to skip date and pull total net PNL from column B. Made sure to specify [1] on both totalNet and previousNet to read from column 2.  

  In order to determine total months included in dataset, made formula to calculate totalMonths +=1. This is the same as totalMonths = totalMonths +1, but shortened. 

  Also included formula to determine net total of PNL for the period. Needed to specify this as an integer so will recognize values when calculating. 

  Determined average change by calculating each - previousNet to determine the net change for each row.

  Net used the average change to determine the greatest increase, and the greatest decrease in profits

  Created a variable to determine the average of monthly changes. Totaled all net changes and divided by total length of the list. Rounded to 2 decimals to match results shown on prompt. 

  Printed out the solutions in the dataset using f strings

  Output the answers to a txtfile to later upload to github.

  
README - pyPoll

  Initially included imports for OS and CSV. 

  Then specified path for botht the CSV file and Txt File. 

  Added formula to read the CSV and convert it to a list

  Determined the header to exclude from calculations

  Needed to include values for each term used in formulas below 

  Needed to create lists for each column, and results lists

  Created first loop to loop through rows in the CSV file

  Specified the row for each list created above, and appended each list 

  Calculated total votes by counting the length of the ballot ID column

  Then looped through each candidate and added in if formula to determine each candidted voted for

  Added in "X" to take the length of candidate names. If printing, result shows as 3 correctly counting the total # of names. 

  Created a second loop to determine each candidate, and their total # of votes within the range. 

  Added in third loop to determine the winner, loser, and percentage for each. Used if formula to determine which candidate had the most votes, the percentage of votes they won, and how many votes they had total. 

  Created foruth loop to display results. Made a list cith the names, percentage, and total votes. After this loop, added electionResults to include "\n" to split into separate rows and join each result matching prompt. 

  Created a formula with f strings to print results

  added refults to text file
