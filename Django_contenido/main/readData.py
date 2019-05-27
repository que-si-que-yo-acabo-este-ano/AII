import os
from Django_contenido.settings import STATIC_ROOT

def readFile(file):
    res = []
    with open(file,encoding="utf-8", errors="ignore") as File:
        rows = File.readlines()
        for row in rows:
            row = row.strip().split('\t')
            res.append(row)
    return res[1:]



tagPath = os.path.join(STATIC_ROOT,"data/tags.dat")
tags = readFile(tagPath)
print(tags)

artistPath = os.path.join(STATIC_ROOT,"data/artists.dat")
artists = readFile(artistPath)
print(len(artists))

userArtistsPath = os.path.join(STATIC_ROOT,"data/user_artists.dat")
userArtists = readFile(userArtistsPath)
print(len(userArtists))

userTaggedartistsPath = os.path.join(STATIC_ROOT,"data/user_taggedartists.dat")
userTaggedartists = readFile(userTaggedartistsPath)
print(len(userTaggedartists))