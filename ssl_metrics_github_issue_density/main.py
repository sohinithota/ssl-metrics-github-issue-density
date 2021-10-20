import argparse
from argparse import Namespace
from collections import Counter
from datetime import date, timedelta

import matplotlib.pyplot as plt
from pandas import DataFrame
import pandas

plt.rcdefaults()
import matplotlib.pyplot as plt
import numpy as np


def getArgs():
    arg = argparse.ArgumentParser(
        prog="SSL Metrics Issue Density",
        usage="Generate Issue Density metrics",
    )

    arg.add_argument(
        "-c",
        "--commits",
        required=True,
        type=open,
        help="Commits JSON file",
    )
    arg.add_argument(
        "-i",
        "--issues",
        required=True,
        type=open,
        help="Issues JSON file",
    )

    args = arg.parse_args()
    return args

def loadData(filename: str) -> DataFrame:
    return pandas.read_json(filename)

# get the LOC from issues file
def getDeltaLOC(commitsDF: DataFrame) -> DataFrame:
    return commitsDF["delta_loc"]


# get the day from issues file
def getDay(commitsDF: DataFrame) -> DataFrame:
    return commitsDF["day_since_0"]


def get_created_at_from_issues(file) -> list:
    return [commits["created_at"] for commits in file]
    # return [commits["closed_at"] for commits in file]


# gets day value from commits.json and converts to a date type starting at project start
# removes repeats of dates
def day_to_date(file) -> list:
    result = []
    days = [commits["day"] for commits in file]
    # hyper-api begain april 28 2020 with 4 commits
    for day in days:
        start = date(2020, 4, 28)
        delta = timedelta(day)
        offset = start + delta
        offset = offset.strftime("%Y-%m-%d")
        result.append(offset)
    #  days.append(offset)
    #  print(days)
    return result


# graph that aggregates all commits on a specific day
def aggregate_commits_graph(file) -> list:
    # for each element in count, if the first index is a date, store it in lx
    # ly = y values
    # the immediate next element ties to this
    count = dict(Counter(file))
    print(count)
    # https://realpython.com/iterate-through-dictionary-python/#iterating-through-items
    # iterate through dictionary values and keys- keys will be x, values will be y
    for key in count.keys():
        print(key, "->", count[key])


def main():
    args: Namespace = getArgs()

    commitsDF: DataFrame = loadData(filename=args.commits)
    issuesDF: DataFrame = loadData(filename=args.issues)

    getDeltaLOC(commitsDF=commitsDF)
    getDay(commitsDF=commitsDF)

    # loc_sum = get_loc_sum_from_issues(issuesDF)
    # get_day = get_day_from_commits(commitsDF)
    # data1 = day_to_date(commitsDF)  ##days of commits
    # get_created_at_from_issues(issuesDF)
    # aggregate_commits_graph(data1)
    # get the value LOC_sum from commits.json


if __name__ == "__main__":
    main()


# get values from both files:
# issues.json: created_at/updated_at/closed_at (for timeline), user (attached to each)
# commits.json: LOC_sum (module size),  day (for timeline) - DONE
# create timeline of commits, in between put issues
