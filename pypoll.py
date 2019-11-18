import os
import csv

csvpath = os.path.join(r'C:\Users\tiffa\downloads\poll_data.csv')
with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    candidates = {}
    Count = 0
    Casted = 0
    percent = 0
    Most_Votes = 0
    
    for row in csvreader:
               
        candidate = row[2]
        Count += 1
        if candidate in candidates.keys():
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

    print("Election Results")
    print("-------------------------------")
    print(f"Total Votes: {Count}")
    print("-------------------------------")
    for candidate in candidates:
        Casted  = candidates[candidate]
        percent = (candidates[candidate])/(Count) * 100
        print(f"{candidate}: {int(percent)}% ({Casted})")
        if candidates[candidate] > Most_Votes:
            Most_Voted = candidate
            Most_Votes = candidates[candidate]
    print("-------------------------------")
    print(f"Winner: {Most_Voted}")    
    print("-------------------------------")
    
    