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
labels = [
    "Debit card",
    "Credit card",
    "Business card",
    "Collectible card game",
    "Penalty card",
    "Telephone card",
    "Payment card",
]
labels_r = [
    "/m/02h5d",
    "/m/0d7pp",
    "/m/01sdgj",
    "/m/0216z",
    "/m/02wvcj0",
    "/m/066zr",
    "/m/09vh0m",
]
labels_and_imageed_human = pd.read_csv(
    "./V2/data/oidv6-train-annotations-human-imagelabels.csv"
)
labels_and_imageed = (
    labels_and_imageed_human.append(
        pd.read_csv("./V2/data/test-annotations-machine-imagelabels.csv")
    )
    .append(pd.read_csv("./V2/data/validation-annotations-machine-imagelabels.csv"))
    .append(pd.read_csv("./V2/data/test-annotations-human-imagelabels (1).csv"))
    .append(pd.read_csv("./V2/data/validation-annotations-human-imagelabels.csv"))
)
imageids = []

for labelname, imageid in tqdm(
    zip(labels_and_imageed["LabelName"], labels_and_imageed["ImageID"])
):
    if labelname in labels_r:
        idx_1 += 1
        imageids.append(imageid)
del labels_and_imageed
del labels_and_imageed_human
bboxs = (
    pd.read_csv("./V2/data/oidv6-train-annotations-bbox.csv")
    .append(pd.read_csv("./V2/data/test-annotations-bbox.csv"))
    .append(pd.read_csv("./V2/data/validation-annotations-bbox.csv"))
)
print(len(bboxs))
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
del bboxs
images_and_bbox_and_imgid_ = pd.DataFrame(
    images_and_bbox_and_imgid_, columns=["ImageID", "XMin", "YMin", "XMax", "YMax"]
)
print(len(images_and_bbox_and_imgid_))
image_urls = (
    pd.read_csv("./V2/data/oidv6-train-images-with-labels-with-rotation.csv")
    .append(pd.read_csv("./V2/data/validation-images-with-rotation.csv"))
    .append(pd.read_csv("./V2/data/test-images-with-rotation.csv"))
)
print(len(image_urls))
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
            # print(imgid)
            data["XMin"].append(imgid_of_iabaid_iter["XMin"])
            data["YMin"].append(imgid_of_iabaid_iter["YMin"])
            data["XMax"].append(imgid_of_iabaid_iter["XMax"])
            data["YMax"].append(imgid_of_iabaid_iter["YMax"])
del images_and_bbox_and_imgid_
# print(data)
data = pd.DataFrame(data)
data.to_csv("./V2/data/Cleaned-Data.csv", index=False)
