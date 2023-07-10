import pandas as pd
import re
dataset=pd.read_fwf('input.txt', header=None)
dataset.columns = ["ID"]
for row_num, object in zip(dataset.index, dataset["ID"].str.findall(r'(.)(?=.+\1)')):
    for letter in object:
        print(dataset.iloc[row_num:0].values[0])
        break
