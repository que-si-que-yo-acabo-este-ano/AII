import csv
import os

def readFile(file):
    res = []
    with open(file,encoding='utf-8') as File:
        reader = csv.DictReader(File)
        for row in reader:
            if "movie" in file:
                row["genres"] = row["genres"].split("|")
            res.append(row)
    return res
