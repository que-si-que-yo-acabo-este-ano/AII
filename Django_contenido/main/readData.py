
def readFile(file):
    res = []
    with open(file,encoding="utf-8", errors="ignore") as File:
        rows = File.readlines()
        for row in rows:
            row = row.strip().split('\t')
            res.append(row)
    return res[1:]

def readUserArtistTagFile(file):
    res = []
    with open(file,encoding="utf-8", errors="ignore") as File:
        rows = File.readlines()
        for row in rows:
            row = row.strip().split()
            res.append(row)
    return res[1:]
