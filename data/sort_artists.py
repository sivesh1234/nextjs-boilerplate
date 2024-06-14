import csv

artists = {}
with open("./artists_2.csv", 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        artists[row[0].upper()] = {"bio": row[1], "problem": row[2], "matches": row[3]}
        
artists_list = list(artists.keys())

artists_list = sorted(artists_list)

with open("./artists_2_sort.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["name", "bio", "problem", "matches"])
    for artist in artists_list:
        row = artists[artist]
        print(row)
        writer.writerow(list((artist, row["bio"], row["problem"], row["matches"])))