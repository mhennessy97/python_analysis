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

  
