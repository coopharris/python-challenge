import os
import csv

#Establishing file Paths
csvpath = os.path.join('C:\\Users\\coopk\\OneDrive\\Desktop\\python-challenge\\PyPoll\\Resources\\election_data.csv')
export_file = os.path.join('C:\\Users\\coopk\\OneDrive\Desktop\\python-challenge\\PyPoll\\analysis\\results.txt')

#open csv file
with open(csvpath) as csvfile :
    csvreader = csv.reader(csvfile)

    #Skip header
    next(csvreader)

    #Assign variables
    candidate_votes = {}
    listofcandidates = []

    #loop through each row
    for rows in csvreader :
              
        #Tracking list of candidates 
        candidate = rows[2]
        if candidate not in listofcandidates :
            listofcandidates.append(candidate)

        # tracking individual vote counts for each candidate
        if candidate in candidate_votes :
            candidate_votes[candidate] += 1
        else :
            candidate_votes[candidate] = 1

#Sum of all votes to find total
total_votes = sum(candidate_votes.values())

# finding the winner with the most votes
winner = max(candidate_votes, key=candidate_votes.get)


# Printing Election header
print(f'''
Election Results 

Total Votes: {total_votes}
''')

# Looping to find candidate's votes and percentage of total votes
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f'{candidate}: {votes} votes ({percentage: .3f}%) of total votes')

# Printing winner
print(f'Winner: {winner}')

#Exporting Results to text file. 
with open(export_file, 'w') as file:
    file.write(f''' 
               Election Results
               
               Total Votes: {total_votes}
               
               ''')
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        file.write(f'{candidate}: {votes} votes ({percentage: .3f}%) of total votes')
        
        file.write(f' Winner: {winner}')