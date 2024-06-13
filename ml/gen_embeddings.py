import csv

import torch
from takeoff_client import TakeoffClient

client = TakeoffClient(port=4000)

artist_file = "../data/artists.csv"
model= "jina"
model_dim = 768

# load artists data
artists = []
with open(artist_file, 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        artists.append({"name": row[0], "bio": row[1]})
        
num_artists = len(artists)
        
embeddings_matrix = torch.zeros(num_artists, model_dim)

batch_size = 64

for i in range(0, num_artists, batch_size):
    start = i
    end = min(i + batch_size, num_artists)
    
    print(f"Processing artists {start} to {end}")
    
    batch_artists = artists[start:end]
    
    response = client.embed([artist['bio'] for artist in batch_artists], consumer_group="embed")
    
    embeddings = response['result']
    
    embeddings_matrix[start:end] = torch.tensor(embeddings)
        
print("Saving embeddings matrix")

# print num zero elelments
print("Number of zero elements in embeddings matrix")
print(torch.sum(embeddings_matrix == 0))
print("Total entries in embeddings matrix")
print(torch.numel(embeddings_matrix))

torch.save(embeddings_matrix, f"../recc_engines/artist_embeddings-{model}.pt")