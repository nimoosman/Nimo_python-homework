#Nimo PyPoll Homework 
# 18 June 2019


import os
import csv


election_data = os.path.join('..', 'Python-Homework', 'election_data.csv')

candidates = []
votes = []
correy_vote = 0
otooley_vote = 0
khan_vote = 0
li_vote = 0
total_vote = 0

with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

  
    for rows in csvreader:
        candidates.append(rows[1])
        votes.append(rows[0])
        
        total_vote +=1
        if rows[2] == "Correy": 
            correy_vote +=1
        elif rows[2] == "O'Tooley":
            otooley_vote +=1
        elif rows[2] == "Khan": 
            khan_vote +=1
        elif rows[2] == "Li":
            li_vote +=1
            
            

print("Election Results")
print("==============================================")

total_vote = len(candidates)

print("Total number of votes cast: " + str(total_vote))


       
correy_percentage = (correy_vote/total_vote) *100
print(f"Correy: {correy_percentage:.2f}% ({correy_vote})")
otooley_percentage = (otooley_vote/total_vote) *100
print(f"O'Tooley: {otooley_percentage:.2f}% ({otooley_vote})")
khan_percentage = (khan_vote/total_vote) *100
print(f"Khan: {khan_percentage:.2f}% ({khan_vote})")
li_percentage = (li_vote/total_vote) *100
print(f"Li: {li_percentage:.2f}% ({li_vote})") 
print("============================================")

if khan_percentage > correy_percentage:
    print("Khan is the Winner!")
elif correy_percentage > khan_percentage:
    print("Correy is the winner!")

#Output as txt file

Efile = open("PyPoll.txt","w")

Efile.write("Ellection Results")

Efile.write("============================================")

Efile.write("Correy: {correy_percentage:.2f}%" + str(correy_vote))

Efile.write("O'Tooley: {otooley_percentage:.2f}% ({otooley_vote})")

Efile.write("Khan: {khan_percentage:.2f}% ({khan_vote})")

Efile.write("Li: {li_percentage:.2f}% ({li_vote})")

Efile.write("============================================")

Efile.write("Khan is the winner!")

#End PyPoll Homework 