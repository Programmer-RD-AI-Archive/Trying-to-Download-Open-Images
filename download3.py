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
split = 750000
labels = [
    "Business card",
    "Collectible card game",
    "Debit card",
    "Penalty card",
    "Telephone card",
]
labels_r = ["/m/01sdgj", "/m/0216z", "/m/02h5d", "/m/02wvcj0", "/m/066zr"]
labels_and_imageed_human = pd.read_csv(
    "./V2/data/test-annotations-human-imagelabels (1).csv"
)
labels_and_imageed_machone = pd.read_csv(
    "./V2/data/test-annotations-machine-imagelabels.csv"
)  # TODO : Change this to machine
labels_and_imageed = labels_and_imageed_machone.append(labels_and_imageed_human)
imageids = []

for labelname, imageid in tqdm(
    zip(labels_and_imageed["LabelName"], labels_and_imageed["ImageID"])
):
    if labelname in labels_r:
        idx_1 += 1
        imageids.append(imageid)
bboxs = pd.read_csv("./V2/data/test-annotations-bbox.csv")
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
image_urls = pd.read_csv("./V2/data/test-images-with-rotation.csv")[
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
        imgid_of_iabaid = images_and_bbox_and_imgid_[
            images_and_bbox_and_imgid_["ImageID"] == imgid[0]
        ]
        for idx_3 in range(len(imgid_of_iabaid)):
            imgid_of_iabaid_iter = images_and_bbox_and_imgid_[
                images_and_bbox_and_imgid_["ImageID"] == imgid[0]
            ].iloc[idx_3]
            data["ImageID"].append(imgid[0])
            data["OriginalURL"].append(imgid[1])
            data["OriginalLandingURL"].append(imgid[2])
            print(imgid)
            data["XMin"].append(imgid_of_iabaid_iter["XMin"])
            data["YMin"].append(imgid_of_iabaid_iter["YMin"])
            data["XMax"].append(imgid_of_iabaid_iter["XMax"])
            data["YMax"].append(imgid_of_iabaid_iter["YMax"])
print(data)
data = pd.DataFrame(data)
data.to_csv("./V2/data/Cleaned-Data.csv", index=False)
