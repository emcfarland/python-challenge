# python-challenge

This project uses Python coursework to analyze two scenarios: monthly losses and gains in a bank (PyBank) and poll results of a small election (PyPoll). It requires understanding of Python syntax and ability to read and write files on relative paths.

## PyBank
After opening the CSV, this script loops through each line of the file and 
  * increments number of rows,
  * adds to the total money moved, 
  * finds the change in profit from the previous month and adds it to the previous total change,
  * stores the current change in profit (current month) if it is worse than any previous month's or better than any previous month's,

Then, the script prints the results for number of months, total money lost/gained, average change, and greatest increase and decrease in profits.

Finally, a text file is written to display the same information as the print statements.

## PyPoll
After opening the CSV, this script loops through each line of the file and 
  * increments the total number of votes,
  * adds candidates' names to dictionary keys if they are not already present,
  * increments each candidate's individual vote counts as dictionary values,

Then, candidates are sorted in decreasing order of individual vote count, and each candidate's name, percentage, and total votes are displayed. The winner is determined by the first key from the sorted candidate dictionary.

Finally, the results are written to a text file to display the same information as the print statements.
