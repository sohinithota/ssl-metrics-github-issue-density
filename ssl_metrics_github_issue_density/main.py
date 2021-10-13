import argparse
import json
import ast

def getArgs1():
    argparse1 = argparse.ArgumentParser(
        prog = "SSL Metrics Density Issues", usage = "Generate metrics based on Density issues"
    )
    argparse1.add_argument("-j", "--jsonfile1", required = True, type = open, help = "first json for this project- commits one.")
    argparse1.add_argument("-j2", "--jsonfile2", required = True, type = open, help = "second json for this project- issues one.")
    
    args1 = argparse1.parse_args()
    return args1
    
# def getArgs2():
    argparse1 = argparse.ArgumentParser(
        prog = "SSL Metrics Density Issues", usage = "Generate metrics based on Density issues"
    )
   # argparse1.add_argument("-j", "--jsonfile1", required = True, type = open, help = "first json for this project- commits one.")
    argparse1.add_argument("-j", "--jsonfile2", required = True, type = open, help = "second json for this project- issues one.")
    
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
    return ([issues["loc_sum"] for issues in file])

#get the day from issues file
def get_day_from_commits(file)-> list:
    return ([issues["day"] for issues in file])

def get_created_at_from_issues(file)-> list:
    return ([commits["created_at"] for commits in file])
    return ([commits["closed_at"] for commits in file])
    return ([commits["updated_at"] for commits in file])

# def get_created_at_from_commits(file)-> list:
    print (file[len(file)-1]["created_at"])


def main():
    args = getArgs1()
    jsonfile1 = args.jsonfile1.name #commits.json
    data1 = import_data_commits(jsonfile1)
    loc_sum = get_loc_sum_from_issues(data1)
    get_day = get_day_from_commits(data1)
   # args = getArgs2()
    jsonfile2 = args.jsonfile2.name #issues.json
    data2 = import_data_issues(jsonfile2)
    get_created_at_from_issues(data2)
    #get the value LOC_sum from commits.json
    
if __name__ == "__main__":
    main()


#get values from both files:
#issues.json: created_at/updated_at/closed_at (for timeline), user (attached to each)
#commits.json: LOC_sum (module size),  day (for timeline) - DONE
# create timeline of commits, in between put issues
