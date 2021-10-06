# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%



# %%
idx = 0


# %%
import pandas as pd

labels = [
    "Business card",
    
    "Collectible card game",
    "Debit card",
    "Penalty card",
    "Greeting card",
    "Telephone card",
]
labels_r = ["/m/01sdgj", "/m/0216z", "/m/02h5d", "/m/02wvcj0", "/m/03r8dh", "/m/066zr"]


# %%
get_ipython().system('ls')


# %%
annotations = pd.read_csv('./data/oidv6-train-annotations-human-imagelabels.csv')


# %%
annotations


# %%
bs = []


# %%
for a,b in zip(annotations['LabelName'],annotations['ImageID']):
    if a in labels_r:
        idx += 1
    bs.append(b)


# %%
idx


# %%
annotations = pd.read_csv('./data/oidv6-train-annotations-bbox.csv')


# %%
idx = 0


# %%
for imgid in annotations['ImageID']:
    if imgid in bs:
        idx += 1


# %%
idx


# %%
len(labels)


# %%
annotations[annotations['LabelName'] == '/m/02wvcj0']


# %%



# %%



# %%



