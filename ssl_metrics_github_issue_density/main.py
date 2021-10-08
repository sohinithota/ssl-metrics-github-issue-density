import argparse
import json

def getArgs():
    argparse1 = argparse.ArgumentParser(
        prog = "SSL Metrics Density Issues", usage = "Generate metrics based on Density issues"
    )
    argparse1.add_argument("-j", "--json", required = True, type = open, help = "json file created through LOC"
    )
    args = argparse1.parse_args()
    return args

def import_data():
    f = open('issues.json',)
    data = json.load(f)
    for i in data[0]:
        print(i)
    f.close()


def main():
    args = getArgs()
    import_data()

if __name__ == "__main__":
    main()

'''
## get values from both files:
issues.json: created_at/updated_at/closed_at (for timeline), user (attached to each)
commits.json: LOC_sum (module size),  day (for timeline)
## create timeline of commits, in between put issues
