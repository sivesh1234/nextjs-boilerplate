import csv

import torch

artist_file = "../data/artist_bios_sorted.csv"
model = "jina"
recc_engine = torch.load(f"../recc_engines/similarity_matrix-{model}.pt")
artists = {}
ordered_names = []

with open(artist_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        artists[row[0]] = row[1]
        ordered_names.append(row[0])
        
        
        
class ArtistManager():
    
    def __init__(self):
        self.artists = artists
        self.ordered_names = ordered_names
        self.recc_engine = recc_engine
        
    def get_reccs(self, names, k):
        name_indexes = [self.ordered_names.index(name.upper()) for name in names]
        num_artists = len(self.ordered_names)
        
        print("Num artists: ", num_artists)
        
        # Get indexes of our top Artists
        indexes = torch.tensor(name_indexes)
        print("Indexes: ", indexes)
        
        # Get similarity matrix rows
        artist_rows = self.recc_engine[indexes]
        
        # Remove recomendation to self
        artist_rows[torch.arange(len(names)), indexes] = 0
        
        print("Artist rows: ", artist_rows)
        
        # Flatten the matrix
        flat = artist_rows.flatten()
        
        # Get the sorted list of indexes
        sorted_indexes = torch.argsort(flat, descending=True)
        
        print(sorted_indexes)
        
        recc_artists = {}
        

        for index in sorted_indexes:
            row = index // num_artists
            col = index % num_artists
            
            artist = self.ordered_names[col]
            recc_from = names[row].upper()

            if artist not in recc_artists:
                recc = {'name': artist, 'bio': self.artists[artist], 'recc_from': [recc_from]}
                recc_artists[artist] = recc
            else:
                recc_artists[artist]['recc_from'].append(recc_from)
                
            if len(recc_artists) == k:
                break
            
        print(recc_artists)
            
        return list(recc_artists.values())
        
        
        
        
artist_manager = ArtistManager()

if __name__ == "__main__":
    
    reccs = artist_manager.get_reccs(["BENJI B", "47SOUL"], 5)
    
    print(reccs)