import csv
import numpy as np

def isnum(a):
    try:
        float(a)
    except ValueError:
        return False
    return True

movies = []
with open('movies.csv', 'rb') as csvfile:
    moviereader = csv.reader(csvfile)
    for row in moviereader:
        movies.append(row)

movies = np.array(movies)
wwgross = np.array([x for x in movies[1:,2] if isnum(x)]).astype(np.float)
wwGrossStats = (np.mean(wwgross), np.median(wwgross))
print wwGrossStats

