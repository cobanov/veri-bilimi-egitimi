import pandas as pd

df = pd.read_csv("./penguins_scaled.csv")

print(df.head())

classes = {0: [0, 1, 1], 1: [1, 0, 0], 2: [1, 1, 1]}
colors = pd.DataFrame(df["target"].map(classes).tolist(), columns=["v1", "v2", "v3"])

classes = {0: [0, 1, 1], 1:[1, 0, 1], 2:[1, 2wef wef
qwefkmqpowef 
wel;fk mm]qwef
]}