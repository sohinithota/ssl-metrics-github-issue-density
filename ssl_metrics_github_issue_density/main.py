import argparse
import json
from datetime import date, timedelta
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def getArgs1():
    argparse1 = argparse.ArgumentParser(
        prog = "SSL Metrics Density Issues", usage = "Generate metrics based on Density issues"
    )
    argparse1.add_argument("-j", "--jsonfile1", required = True, type = open, help = "first json for this project- commits one.")
    argparse1.add_argument("-j2", "--jsonfile2", required = True, type = open, help = "second json for this project- issues one.")
    
    args1 = argparse1.parse_args()
    return args1

#used this method in previous productivity project, it takes in the JSON as a list to be manipulated later. I store data for both files in this project.
def import_data_commits(filename: str = "commits.json") -> list:
    with open(file = filename, mode= "r") as fp:
        return (json.load(fp))

def import_data_issues(filename: str = "issues.json") -> list:
    with open(file = filename, mode= "r") as fp:
        return (json.load(fp))

#get the LOC from issues file
def get_loc_sum_from_issues(file)-> list:
    return ([issues["delta_loc"] for issues in file])
#get the day from issues file
def get_day_from_commits(file)-> list:
    return ([commits["day"] for commits in file])

def get_created_at_from_issues(file)-> list:
    return ([commits["created_at"] for commits in file])
    return ([commits["closed_at"] for commits in file])
    return ([commits["updated_at"] for commits in file])

#gets day value from commits.json and converts to a date type starting at project start
#removes repeats of dates 
def day_to_date(file) -> list:
    result = []
    days= ([commits["day"] for commits in file])
    #hyper-api begain april 28 2020 with 4 commits
    for day in days:
        start = date(2020,4,28)
        delta = timedelta(day)
        offset = start + delta
        offset = (offset.strftime('%Y-%m-%d'))
        result.append(offset)
      #  days.append(offset)
      #  print(days)
    return(result)

def create_graph(file) -> list:
    print(file)

def main():
    args = getArgs1()
    jsonfile1 = args.jsonfile1.name #commits.json
    data1 = import_data_commits(jsonfile1)
    loc_sum = get_loc_sum_from_issues(data1)
    get_day = get_day_from_commits(data1)
    data1 = day_to_date(data1) ##days of commits
    jsonfile2 = args.jsonfile2.name #issues.json
    data2 = import_data_issues(jsonfile2)
    get_created_at_from_issues(data2)
    create_graph(data1)
    #get the value LOC_sum from commits.json
    
if __name__ == "__main__":
    main()


#get values from both files:
#issues.json: created_at/updated_at/closed_at (for timeline), user (attached to each)
#commits.json: LOC_sum (module size),  day (for timeline) - DONE
# create timeline of commits, in between put issues
