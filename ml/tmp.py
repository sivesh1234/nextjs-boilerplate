import csv

artists = {}
with open("../data/artist_bios.csv", 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        artists[row[0].upper()] = row[1]
        
artists_list = list(artists.items())

artists_list = sorted(artists_list, key=lambda x: x[0])

with open("../data/artist_bios_sorted.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["name", "bio"])
    for artist in artists_list:
        writer.writerow(artist)