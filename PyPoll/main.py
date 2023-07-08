import csv

# Read the election data from CSV file
def read_election_data(file_path):
    election_data = []
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            election_data.append(row)
    return election_data

# Perform vote analysis on the election data
def analyse_election_data(election_data):
    total_votes = len(election_data)
    candidates = {}
    winner = {"name": "", "votes": 0}

    # Iterate over election data
    for row in election_data:
        candidate = row["Candidate"]

        # Update candidate's vote count
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

        # Check for the winner
        if candidates[candidate] > winner["votes"]:
            winner["name"] = candidate
            winner["votes"] = candidates[candidate]

    # Calculate the percentage of votes each candidate won
    percentage_votes = {}
    for candidate, votes in candidates.items():
        percentage_votes[candidate] = (votes / total_votes) * 100

    # Format the analysis results
    analysis_results = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""

    for candidate, votes in candidates.items():
        percentage = percentage_votes[candidate]
        analysis_results += f"{candidate}: {percentage:.3f}% ({votes})\n"

    analysis_results += f"""
-------------------------
Winner: {winner["name"]}
-------------------------
"""

    return analysis_results

# Write the analysis results to a text file
def write_analysis_results(file_path, analysis_results):
    with open(file_path, "w") as txtfile:
        txtfile.write(analysis_results)

# Main function
def main():
    file_path = "election_data.csv"
    output_file = "election_analysis.txt"

    # Read election data
    election_data = read_election_data(file_path)

    # Perform analysis on election data
    analysis_results = analyse_election_data(election_data)

    # Print analysis to terminal
    print(analysis_results)

    # Write analysis results to text file
    write_analysis_results(output_file, analysis_results)

# Run the program
if __name__ == "__main__":
    main()
