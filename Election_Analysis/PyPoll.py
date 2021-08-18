# The data we need to retrieve.
#Add our dependencies.
import csv
import os

#assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize total_votes
total_votes = 0
#define Candidate Options
candidate_options = []
#define candidate votes dictionary
candidate_votes = {}
#define the winning candidate and winning count tracker
winning_candidate = " "
winning_count = 0
winning_percentage = 0

# open the election results and read the file.
with open(file_to_load) as election_data: 
    
    #read the file
    file_reader = csv.reader(election_data)
    
    #read and print the header row
    headers = next(file_reader)
    
    #print each row in the CSV file
    for row in file_reader:
        total_votes += 1
        # print candidate name from each row
        candidate_name = row[2]
        # if the candidate does not match any existing candidate....
        if candidate_name not in candidate_options:
            # add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        #add a vote to htat candidate's count
        candidate_votes[candidate_name] += 1
    
    #save the results to our text file.
    with open(file_to_save,"w") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        #save the final vote count to the text file.
        txt_file.write(election_results)
        


        #determine the percentage of votes for each candidate by looping through the counts.
        #1. interate through the candidate list.
        for candidate_name in candidate_votes:
            #2. retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
            #3. calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100

            #print out each candidate's name, vote count, and percentage of votes to the terminal
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            #print each candidate, their voter count, and the percentage to the terminal.
            print(candidate_results)
            #save the candidate results to our text file.
            txt_file.write(candidate_results)

            ##determine the winning vote count and candidate
            #1. determine if the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                    #2. if ture, then set winning_count = votes and winning_percentage = vote_percentage
                    winning_count = votes
                    winning_percentage = vote_percentage
                    #3. set the winning_candidate equal to the candidate's name
                    winning_candidate = candidate_name
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Vote Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        #save winning summary to txt file
        txt_file.write(winning_candidate_summary)
    
