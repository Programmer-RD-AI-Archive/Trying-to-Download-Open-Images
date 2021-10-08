import pandas as pd
from tqdm import tqdm

# annotations = pd.read_csv("./V2/data/oidv6-train-images-with-labels-with-rotation.csv")[
#     :1000
# ]
# # for row in tqdm(annotations.iteritems()):
# #     # row = row.tolist()
# #     # print(row['ImageID'])
# #     print(list(row))
# #     break

# # print(annotations[annotations["ImageID"] == "d05c3e451f79174d"])
# print(annotations.query('ImageID == "d05c3e451f79174d"')['ImageID'][1])
# print(annotations.query('ImageID == "d05c3e451f79174d"')['Subset'][1])
# print(annotations.query('ImageID == "d05c3e451f79174d"').columns)
annotations = pd.read_csv("./V2/data/oidv6-train-annotations-bbox.csv")[:1000]
print(annotations.query('ImageID == "d05c3e451f79174d"'))
