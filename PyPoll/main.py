import os
import csv

#opening the doc, one level up in Resources folder
poll = os.path.join("Resources", "election_data.csv")

#set opening values to 0, name variables and dictionary
votes = 0
candidate_list=[]
name=[]
results_dict={}


# Open and read csv (be sure you have correct delimiter)
with open(poll) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
     # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
      # Read through each row of data after the header
    for row in csv_reader:
        
        #get the total number of votes cast by counting rows- each row it gets to will add one to the count
        votes = votes +1
        #Call row2 name so its easy to identify in below
        name = row[2]
        #read name to build candidate list, if its not there add to list 
        if name not in candidate_list: 
            candidate_list.append(name)
            #Build a dictionary, using the names from the candidate_list as keys
            results_dict[name] = 0
        #add each instance you find name to the key in the dictonary
        results_dict[name] += 1
        #analyze dict
        for k,v in results_dict.items():
            cand_name=k
            cand_vote=v
            cand_percent= round(v/votes*100, 3)

        #find the winner by grabbing the key with the max value in the dictionary 
        winner=max(results_dict, key=results_dict.get)

        #The winner of the election based on popular vote.
    print("Election Results")
    print("------------------------------------")
    print(f"Total Votes: {votes}")
    print("------------------------------------")
    for k,v in results_dict.items(): 
        print(f"{k}: {round(v/votes*100, 3)}% ({v})")
    print("------------------------------------")
    print(f"Winner: {winner}")
    print("------------------------------------")

# Specify the path and name of file to write
output_path = os.path.join("Analysis", "poll_results.csv")

with open(output_path, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    #write headers
    writer.writerow(["Total Votes", "Candidate", "Percent of Total Vote", "Votes", "Winner"])
    #write results
    writer.writerow([votes, cand_name, cand_percent, cand_vote, winner])
    #writing to csv only gives me the final of the four names of candidates, something simple I'm missing I'm sure but 
    #DictWriter is my most educated guess, but I had trouble getting it to give me anything different.