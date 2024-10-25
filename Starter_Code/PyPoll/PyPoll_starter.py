# -*- coding: UTF-8 -*-
# create a Python script that analyzes the votes and calculates each of the following values:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_options = []  # Track the candidate options
candidate_votes = {}  # Track the candidate votes
winning_candidate = ""  # Track the winning candidate
winning_count = 0  # Track the winning vote count
winning_percentage = 0  # Track the winning candidate's percentage


# Define lists and dictionaries to track candidate names and vote counts
# Candidate Options and Vote Counters
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    
    # Print a loading indicator (for large datasets)
    print(". ", end="")

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        
        # Increment the total vote count for each row
        total_votes += 1
        
        # Get the candidate's name from the row
        candidate_name = row[2]
        
        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
            
        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1
        
# Open a text file to save the output
with open(file_to_output, "w") as txt_file:    

    # Print the total vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Write the total vote count to the text file
    txt_file.write(election_results)
    
    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_votes:
        
        # Get the vote count and calculate the percentage
        votes = candidate_votes[candidate]
        vote_percentage = (votes / total_votes) * 100
        
        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

            # Print the candidate's results to the terminal
        candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(candidate_results, end="")

            
        # Print and save each candidate's vote count and percentage
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        txt_file.write(voter_output)
        
    # Generate and print the winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary, end="")

    # Save the winning candidate summary to the text file
    txt_file.write(winning_candidate_summary)
