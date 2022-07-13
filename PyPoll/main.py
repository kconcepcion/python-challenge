#importing the libraries
import os
import csv

#initializing variables
totalVotes = 0
candidateList = []
fullCandidateList = []
listPlace = 1
currentCandidate = " "

#reading the file into the code
electionCSV = os.path.join("..", "Resources", "election_data.csv")

with open(electionCSV, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    header = next(csvReader)

    #this for loop iterates through the for csv file to get the total votes, i am also filling two list with the same thing. the candidateList i will use to get the names of the people running and the fullCandidateList I will use to count how many times each name was repreated (which also is the same number has how many times they were voted for)
    for row in csvReader:
        totalVotes +=1
        candidateList.append(row[2])
        fullCandidateList.append(row[2])
    
#creating a complete list of candidates by deleting all the reapeats
candidateList = list(dict.fromkeys(candidateList))

#creating a variable that holds the list length
listLength = len(candidateList)

#creating an empty list with a set size (using listLength) to store all the of candidates vote count
candidateVote = [None] * listLength #candidateVote holds the number of votes each candidate recieved
candidatePercent = [None] * listLength #candidatePercent holds the percentage of votes each candidate recieved

#this variable will hold the winner once calculated
winnerCandidate = " "

#filling the vote count list from the full candidate list using the candidate list as the reference
for i in range(len(candidateList)):
    candidateVote[i] = fullCandidateList.count((candidateList[i]))

#filling a list with the percentage of votes for each candidate
for j in range(len(candidateList)):
    candidatePercent[j] = "{:.03%}".format((candidateVote[j]/totalVotes))

#determining the winning candidate by determining the hightest number in the candidateVote list which holds the total number of votes each candidate has and using it as the index to find the candidate from the candidate list of names
winnerCandidate = candidateList[candidateVote.index(max(candidateVote))]

#printing out all the results
print("Election results")
print("----------------------------")
print("Total Votes:", totalVotes)
print("----------------------------")
#i use a for loop here so that way this code can print out all the candidates results regardless of how many candidates are in the candidateList
for k in range(len(candidateList)):
    print(str(candidateList[k]) + ": " + str(candidatePercent[k]) + " (" + str(candidateVote[k]) + ")")
print("----------------------------")
print("Winner: " + winnerCandidate)
print("----------------------------")

#exporting results as text file
outputFilePyPoll = "finalResultPyPoll.txt"

with open(outputFilePyPoll,"w") as file:
    file.write("Election results\n")
    file.write("----------------------------\n")
    file.write("Total Votes:" + str(totalVotes) + "\n")
    file.write("----------------------------\n")
    for k in range(len(candidateList)):
        file.write(str(candidateList[k]) + ": " + str(candidatePercent[k]) + " (" + str(candidateVote[k]) + ")\n")
    file.write("----------------------------\n")
    file.write("Winner: " + winnerCandidate + "\n")
    file.write("----------------------------\n")