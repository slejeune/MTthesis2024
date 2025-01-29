import pickle
import torch
import io
import numpy as np
import pandas as pd

from sklearn.manifold import TSNE

import matplotlib.pyplot as plt
import seaborn as sns

# A bit of a stupid workaround but if it works it works
class CPU_Unpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == 'torch.storage' and name == '_load_from_bytes':
            return lambda b: torch.load(io.BytesIO(b), map_location='cpu')
        else: return super().find_class(module, name)

lang='de'

#contents = pickle.load(f) becomes...
# contents = CPU_Unpickler(f).load()

path = "/Users/Suzenator/Documents/Uni/M4/MThesis/"
with open(path+"sentrepr/sent_repr_"+lang+"-ru.txt", 'rb') as f: 
        # Call load method to deserialze 
        output = CPU_Unpickler(f).load()

with open(path+"sentrepr/input_"+lang+"-ru.txt", 'rb') as f: 
        # Call load method to deserialze 
        input = CPU_Unpickler(f).load()

with open(path+"sentrepr/tokenizer_"+lang+"-ru.txt", 'rb') as f: 
        # Call load method to deserialze 
        embed = CPU_Unpickler(f).load()

# Perform t-SNE to reduce dimensionality to 2D
tsne = TSNE(n_components=2, perplexity=2)
reduced_embeddings = tsne.fit_transform(output[0][-1][:,-1,:])
df = pd.DataFrame(reduced_embeddings, columns=['Dimension 1', 'Dimension 2'])

# Create a KDE plot
plt.figure(figsize=(10, 8))
sns.kdeplot(data=df, x='Dimension 1', y='Dimension 2', fill=False, thresh=False)
plt.title('2D Kernel Density Estimation of Hidden States')
plt.legend()
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.show()
