import csv
filepath = "resources/election_data.csv"

with open(filepath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    vote_count = 0
    candidates_list = []
    for row in csvreader:

        vote_count = vote_count + 1
        candidates_list.append(row[2])

simplified_candidates = list(set(candidates_list))

individual_votes = []
for i in range(0, len(simplified_candidates)):
    individual_votes.append(candidates_list.count(simplified_candidates[i]))

percentage = []
for j in range(0, len(individual_votes)):
    percentage.append(f"{round(individual_votes[j] / vote_count * 100,3)}%")

consolidated_list = [] 
for x in range(0, len(individual_votes)):
    consolidated_list.append([simplified_candidates[x], percentage[x], individual_votes[x]])

def takeThird(element):
    return element[2]

consolidated_list.sort(key = takeThird, reverse = True)

print ("Election Results")
print ("------------------------")
print (f"Total Votes {vote_count}")
print ("------------------------")
for item in consolidated_list:
    print (f"{item[0]}: {item[1]} ({item[2]})")
print ("------------------------")
print (f"Winner: {consolidated_list[0][0]}")
print ("------------------------")

with open ("PyPoll.txt", "w") as PollResult:
    PollResult.write ("Election Results\n")
    PollResult.write ("----------------------------\n")
    PollResult.write (f"Total Votes {vote_count}\n")
    PollResult.write ("----------------------------\n")
    for item in consolidated_list:
        PollResult.write (f"{item[0]}: {item[1]} ({item[2]}) \n")
    PollResult.write ("----------------------------\n")
    PollResult.write (f"Winner: {consolidated_list[0][0]}\n")
    PollResult.write ("-----------------------------\n")
