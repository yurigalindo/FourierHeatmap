import pandas as pd

all = pd.read_csv("waterbirds/metadata.csv")
reduced = pd.read_csv("waterbirds_filenames.csv")

joined = pd.merge(all,reduced,on='img_filename')

joined.to_csv("reduced_metadata.csv")