import csv

election_data = "PyPoll/Resources/election_data.csv"

with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    firstline= next(csvreader)
    votes = 1
    candidate_list = 0 
    candidates= set()
    vote_percentage=0
    candidate_votes={}
    candidate_name=0
    for row in csvreader:
        votes += 1
        candidates.add(row[2])
        candidate_name = row[2]
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1
    
    output = (
        f"\nElection Results\n"
        f"----------------------------\n"
        f"Total Votes: {votes}\n"
        f"----------------------------\n"
    )
    for candidate, vote_count in candidate_votes.items():
        vote_percentage = (vote_count / votes) * 100
        output += f"{candidate}: {vote_percentage:.2f}% ({vote_count})\n"
    winner = max(candidate_votes, key=candidate_votes.get)
    output += (
        f"----------------------------\n"
        f"Winner: {winner}\n"
        f"----------------------------\n"
    )
    
    print(output)
    
    # Export the results to text file
    file_to_output = "PyPoll/Analysis/Election_Results.txt"
    with open(file_to_output, "w") as txt_file:    
        txt_file.write(output)