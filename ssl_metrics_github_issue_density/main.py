import argparse
import json
import ast

def getArgs1():
    argparse1 = argparse.ArgumentParser(
        prog = "SSL Metrics Density Issues", usage = "Generate metrics based on Density issues"
    )
    argparse1.add_argument("-j", "--jsonfile1", required = True, type = open, help = "first json for this project- commits one.")
   # argparse1.add_argument("-j", "--jsonfile2", required = True, type = open, help = "second json for this project- issues one.")
    
    args1 = argparse1.parse_args()
    return args1
    
def getArgs2():
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


def main():
    args = getArgs1()
    jsonfile1 = args.jsonfile1.name
    data = import_data_commits(jsonfile1)
    args = getArgs2()
    jsonfile2 = args.jsonfile2.name
    data = import_data_issues(jsonfile2)

if __name__ == "__main__":
    main()


#get values from both files:
#issues.json: created_at/updated_at/closed_at (for timeline), user (attached to each)
#commits.json: LOC_sum (module size),  day (for timeline)
# create timeline of commits, in between put issues
