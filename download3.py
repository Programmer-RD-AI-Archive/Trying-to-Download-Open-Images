import pandas as pd
from tqdm import tqdm

idx_1 = 0
idx_2 = 0
idx_3 = 0
data = {
    "ImageID": [],
    "OriginalURL": [],
    "OriginalLandingURL": [],
    "XMin": [],
    "YMin": [],
    "XMax": [],
    "YMax": [],
}
split = 250000
labels = [
    "Business card",
    "Collectible card game",
    "Debit card",
    "Penalty card",
    "Greeting card",
    "Telephone card",
]
labels_r = ["/m/01sdgj", "/m/0216z", "/m/02h5d", "/m/02wvcj0", "/m/03r8dh", "/m/066zr"]
labels_and_imageed = pd.read_csv(
    "./V2/data/oidv6-train-annotations-human-imagelabels.csv"
)[:split]
imageids = []

for labelname, imageid in tqdm(
    zip(labels_and_imageed["LabelName"], labels_and_imageed["ImageID"])
):
    if labelname in labels_r:
        idx_1 += 1
    imageids.append(imageid)
bboxs = pd.read_csv("./V2/data/oidv6-train-annotations-bbox.csv")[:split]
images_and_bbox_and_imgid_ = []
imgids = []
for imgid in tqdm(
    zip(
        bboxs["ImageID"],
        bboxs["XMin"],
        bboxs["YMin"],
        bboxs["XMax"],
        bboxs["YMax"],
    )
):
    if imgid[0] in imageids:
        idx_2 += 1
        images_and_bbox_and_imgid_.append(imgid)
        imgids.append(imgid[0])
images_and_bbox_and_imgid_ = pd.DataFrame(
    images_and_bbox_and_imgid_, columns=["ImageID", "XMin", "YMin", "XMax", "YMax"]
)
print(images_and_bbox_and_imgid_)
image_urls = pd.read_csv("./V2/data/oidv6-train-images-with-labels-with-rotation.csv")[
    :25000
]
for imgid in tqdm(
    zip(
        image_urls["ImageID"],
        image_urls["OriginalURL"],
        image_urls["OriginalLandingURL"],
    )
):
    if imgid[0] in imgids:
        # print(imgids)
        data["ImageID"] = imgid[0]
        data["OriginalURL"] = imgid[1]
        data["OriginalLandingURL"] = imgid[2]
        imgid = images_and_bbox_and_imgid_[
            images_and_bbox_and_imgid_["ImageID"] == imgid[0]
        ].iloc[0]
        print(imgid)
        data["XMin"].append(imgid['XMin'])
        data["YMin"].append(imgid['YMin'])
        data["XMax"].append(imgid['XMax'])
        data["YMax"].append(imgid['YMax'])
print(data)
data = pd.DataFrame(data)
data.to_csv("./V2/data/Cleaned-Data.csv", index=False)
