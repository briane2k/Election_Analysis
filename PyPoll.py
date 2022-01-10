# Add our dependencies.
import csv
import os
from typing import TYPE_CHECKING
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)


    # Read and print the header row.
    headers = next(file_reader)


    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1

#End with election_data


for name in candidate_options:

    percentage_votes = (float(candidate_votes[name]) / float(total_votes)) * 100

    print(f"Candidate: {name} recieved({candidate_votes[name]:,}): {percentage_votes:2.1f}% of the total({total_votes:,}) Votes")

    if(candidate_votes[name] > winning_count):
        winning_count = candidate_votes[name]
        winning_candidate = name
        winning_percentage = percentage_votes

#End for


winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


