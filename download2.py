import pandas as pd
from tqdm import tqdm

idx = 0

labels = [
    "Business card",
    "Collectible card game",
    "Debit card",
    "Penalty card",
    "Greeting card",
    "Telephone card",
]
labels_r = ["/m/01sdgj", "/m/0216z", "/m/02h5d", "/m/02wvcj0", "/m/03r8dh", "/m/066zr"]
annotations = pd.read_csv("./V2/data/oidv6-train-annotations-human-imagelabels.csv")[:25000]
print(annotations.columns)
bs = []
for a, b in tqdm(zip(annotations["LabelName"], annotations["ImageID"])):
    if a in labels_r:
        idx += 1
    bs.append(b)
print(idx)
annotations = pd.read_csv("./V2/data/oidv6-train-annotations-bbox.csv")[:25000]
print(annotations.columns)
idx = 0
idx_other = 0
imgids = []
imageids = []
for imgid in tqdm(
    zip(
        annotations["ImageID"],
        annotations["XMin"],
        annotations["YMin"],
        annotations["XMax"],
        annotations["YMax"],
    )
):
    # print(imgid)
    if imgid[0] in bs:
        idx += 1
        imgids.append(imgid)
        imageids.append(imgid[0])
print(idx)
annotations = pd.read_csv("./V2/data/oidv6-train-images-with-labels-with-rotation.csv")[:25000]
print(annotations.columns)
data = {
    "ImageID": [],
    "OriginalURL": [],
    "OriginalLandingURL": [],
    "XMin": [],
    "YMin": [],
    "XMax": [],
    "YMax": [],
}
for imgid in tqdm(
    zip(
        annotations["ImageID"],
        annotations["OriginalURL"],
        annotations["OriginalLandingURL"],
    )
):
    print(imgid)
    print(imageids)
    break
    if imgid[0] in imageids:
        print(imgids)
        data["ImageID"] = imgid[0]
        data["OriginalURL"] = imgid[1]
        data["OriginalLandingURL"] = imgid[2]
        data["XMin"].append(imgid[1])
        data["YMin"].append(imgid[2])
        data["XMax"].append(imgid[3])
        data["YMax"].append(imgid[4])
# print(imageids)
# print(imgids)
# print(data)
data = pd.DataFrame(data)
data.to_csv("./V2/data/Cleaned-Data.csv", index=False)
