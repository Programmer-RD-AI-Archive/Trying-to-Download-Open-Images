# card
import pandas as pd
from tqdm import tqdm
labels = pd.read_csv('./V2/data/Desc-of-Labels.csv')
newlabelsnames = []
newnames = []
labelsnames = labels['LabelName']
names = labels['DisplayName']
for labelname,name in tqdm(zip(labelsnames,names)):
    if 'card' in name.lower().split(' '):
        newlabelsnames.append(labelname)
        newnames.append(name)
newlabels = pd.DataFrame({'LabelName':newlabelsnames,'DisplayName':newnames})
newlabels.to_csv('./V2/data/New-Desc-of-Labels.csv',index=False)

labels = [
    'Business card',
    'Collectible card game',
    'Debit card',
    'Penalty card',
    'Greeting card',
    'Telephone card',
]
