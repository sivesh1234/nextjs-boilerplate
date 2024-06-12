import csv

artists = {}

with open('../data/artists.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        artists[row[0]] = row[1]