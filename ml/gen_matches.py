import torch
import torch.nn as nn

model = "jina"
embedding_path = f"../recc_engines/artist_embeddings-{model}.pt"

embeddings = torch.load(embedding_path)

eps = 1e-8

normed_embeddings = embeddings / (embeddings.norm(dim=1, keepdim=True) + eps)

similarity_matrix = torch.mm(normed_embeddings, normed_embeddings.t())

print(similarity_matrix.shape)

# save the similarity matrix
similarity_path = f"../recc_engines/similarity_matrix-{model}.pt"
torch.save(similarity_matrix, similarity_path)