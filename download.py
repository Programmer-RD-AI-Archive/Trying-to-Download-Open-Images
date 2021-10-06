

# %%


# %%






# %%



# %%
annotations


# %%



# %%



# %%
idx


# %%
annotations = pd.read_csv('./V2/data/oidv6-train-annotations-bbox.csv')


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



