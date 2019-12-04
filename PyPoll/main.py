import pandas as pd

# Store filepath in a variable
poll_data = "Resources/election_data.csv"

 # Read our Data file with the pandas library
poll_data_df = pd.read_csv(poll_data, encoding="ISO-8859-1")

#Calculate total votes
total_votes = poll_data_df["Voter ID"].count()

#get count by candidates
#default is decending order, so first candidate is the winner
candidate_votes = poll_data_df["Candidate"].value_counts()

#convert series to data frame
candidate_summary_df = candidate_votes.to_frame().reset_index()

#rename column headings
candidate_summary_df.columns = ['Candidates', 'Votes']

#add % column/series to candidate_summary_df
candidate_summary_df["Percentage"] = candidate_summary_df["Votes"]/total_votes
candidate_summary_df["Percentage"] = pd.Series(["{0:.3f}%".format(i * 100) for i in candidate_summary_df["Percentage"]])

#format votes with ()
candidate_summary_df["Votes"] = pd.Series(["(" + str(i) + ")" for i in candidate_summary_df["Votes"]])

#reorder columns
candidate_summary_df = candidate_summary_df[["Candidates", "Percentage", "Votes"]]

#print output
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(candidate_summary_df.to_string(index=False, header=False))
print("-------------------------")
print(candidate_summary_df.iloc[0,0])
print("-------------------------")

#print to text file
print("Election Results", file=open("pypoll_output.txt", "a")) 
print("-------------------------", file=open("pypoll_output.txt", "a"))
print(f"Total Votes: {total_votes}", file=open("pypoll_output.txt", "a"))
print("-------------------------", file=open("pypoll_output.txt", "a"))
print(candidate_summary_df.to_string(index=False, header=False), file=open("pypoll_output.txt", "a"))
print("-------------------------", file=open("pypoll_output.txt", "a"))
print(candidate_summary_df.iloc[0,0], file=open("pypoll_output.txt", "a"))
print("-------------------------", file=open("pypoll_output.txt", "a"))

