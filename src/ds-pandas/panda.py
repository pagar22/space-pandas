import pandas as pd

df = pd.read_csv("data/penguin_sector.csv", index_col=0, sep=",")
print(df)
