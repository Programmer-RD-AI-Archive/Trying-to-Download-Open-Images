idx = 0
import pandas as pd
from tqdm import tqdm
labels = [
    "Business card",
    
    "Collectible card game",
    "Debit card",
    "Penalty card",
    "Greeting card",
    "Telephone card",
]
labels_r = ["/m/01sdgj", "/m/0216z", "/m/02h5d", "/m/02wvcj0", "/m/03r8dh", "/m/066zr"]
annotations = pd.read_csv('./V2/data/oidv6-train-annotations-human-imagelabels.csv')
bs = []
for a,b in tqdm(zip(annotations['LabelName'],annotations['ImageID'])):
    if a in labels_r:
        idx += 1
    bs.append(b)
print(idx)
annotations = pd.read_csv('./V2/data/oidv6-train-annotations-bbox.csv')
idx = 0
idx_other = 0
for imgid,labelname in tqdm(zip(annotations['ImageID'],annotations['LabelName'])):
    if imgid in bs:
        idx += 1
    if labelname in labels_r or labelname in labels:
        idx_other += 1
    labels_r
print(idx)
print(idx_other)
