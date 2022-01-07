# Import the datetime class from the datetime module.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
#election_data = open(file_to_load,'r')
with open(file_to_load) as election_data:

    # perform analysis

    # The data we need to retireve
    # 1 The total number of votes cast
    # 2 A complete list of candidates who recieved votes
    # 3 The percentage of votes each candidate won
    # 4 The total number of votes each candidate won
    # 5 The winner of the election based onb popular vote

    
    # Using the with statement open the file as a text file.
    with open(file_to_save, "w") as txt_file:
        
        # Write some data to the file.
        txt_file.write("Hello World")