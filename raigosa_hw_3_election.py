import os
import csv

# function builds a string of the candidates, votes and percentages from the results dict
def build_votes_string( results, total_votes ):
    votes_string = ""
    for key in results:
        votes = results[key]
        votes_string += f"{key}: {votes/total_votes*100:.3f}% ({votes})\n"
    return votes_string

# function finds candidate in results dict w/ most votes
def find_winner( results ):
    most_votes = 0
    winner = ""
    for key in results:
        if results[key] > most_votes:
            most_votes = results[key]
            winner = key
    return winner

# function builds redsults string
def build_results_string( total_votes, results ):
    results_string = "Election Results\n-------------------------\n\n"
    results_string += f"Total Votes: {total_votes}\n-------------------------\n"
    results_string += f"{build_votes_string(results, total_votes)}-------------------------\n"
    results_string += f"Winner: {find_winner(results)}\n-------------------------\n"
    
    return results_string

election_csv = os.path.join("Pypoll","Resources", "election_data.csv")

# Read in the CSV file
with open(election_csv, 'r') as resultsfile:

    # Split the data on commas
    csvreader = csv.reader(resultsfile, delimiter=',')

    # variables
    total_votes = 0
    results = {}

    # loop thru data, populate variables
    next(csvreader)
    for row in csvreader:
        candidate = row[2]
        total_votes += 1
        if candidate not in results:
            results[candidate] = 1
        else:
            results[candidate] += 1
    
    # build and print results string to terminal
    results_string = build_results_string(total_votes, results)
    print( results_string )

    # save results string as text file
    output_file = open("election_results.txt", "w")
    output_file.write(results_string)
    output_file.close()