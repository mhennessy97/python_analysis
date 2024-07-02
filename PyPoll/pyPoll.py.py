#import CVS and OS
import os
import csv

#load in CSV file for analysis

csvfile = os.path.join(".", "Resources", "election_data.csv")

txtfile = os.path.join(".", "Resources", "election_analysis.txt")


# read the CSV file and convert it to a list

with open(csvfile) as financial_data:
    csvreader = csv.reader(financial_data)
  
    #determine header to exclude from data
    header = next(csvreader)

    #file needs somewhere to begin counting the total # of votes. add in value

    totalVotes = 0
    winnerTotal = 0
    loserTotal = 0
   

    # create lists for each column

    counties = []
    candidates = []
    candidateNames = []
    totalVotesEach = []
    eachCandidate = []
    totalPercentEach = []  

    #determine the total # of votes included in the dataset.  
    for rows in csvreader:
        totalVotes = totalVotes + 1
        

    #read the rows after the header
        county=rows[1]
        candidate=rows[2]
        counties.append(county)
        candidates.append(candidate)

#load in first candidate name to begin comparison
candidateNames.append(candidates[0])

#loop through list of candidates 
for candidateLoop in range (totalVotes-1):
    if candidates[candidateLoop+1] != candidates[candidateLoop] and candidates[candidateLoop+1] not in candidateNames:
        candidateNames.append(candidates[candidateLoop+1])

x = len(candidateNames)

#add second loop to determine each candidate, and their total # of votes
for totalVoteLoop in range (x):
    totalVotesEach.append(candidates.count(candidateNames[totalVoteLoop]))

loserTotal = totalVotes

#add third loop to determine the winner, loser, and the percentage for each
for percentageVoteLoop in range (x):
    totalPercentEach.append(f'{round((totalVotesEach[percentageVoteLoop]/totalVotes*100),3)}%')
    if totalVotesEach[percentageVoteLoop] > winnerTotal:
        winner = candidateNames[percentageVoteLoop]
        winnerTotal = totalVotesEach[percentageVoteLoop]
    if totalVotesEach[percentageVoteLoop] < loserTotal:
        loser = candidateNames[percentageVoteLoop]
        loserTotal = totalVotesEach[percentageVoteLoop]

#add fourth loop to display each candidate name, the percentage of votes won, and the total votes each received
for resultsLoop in range(x):
    eachCandidate.append(f'{candidateNames[resultsLoop]}: {totalPercentEach[resultsLoop]} ({totalVotesEach[resultsLoop]})')

electionResults = '\n'.join(eachCandidate)


#print out the soltions requested from the dataset

solution = (
    f'Election Results\n'
    f'----------------------------\n'
    f'Total Votes: {totalVotes}\n'
    f'----------------------------\n'
    f'{electionResults}\n'
    f'----------------------------\n'
    f'Winner: {winner}\n'
    f'----------------------------'
)

print(solution)

#output and create a text file with soltuions
with open(txtfile, "w") as txt_file:
    txt_file.write(solution)


# In[ ]:




