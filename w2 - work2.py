import pandas as pd

df = pd.read_csv('president_heights.csv')
enuzun= df[df['height(cm)'] == df['height(cm)'].max()]["order"].values
enkısa= df[df['height(cm)'] == df['height(cm)'].min()]["order"].values


print("En uzun boylu başkan", "lar" if len(enuzun)>1 else "", sep="")
for i in enuzun:
    print(i,". başkan", sep="")

print("----------------------")

print("En kısa boylu başkan","lar" if len(enkısa)>1 else "", sep="")
for i in enkısa:
    print(i,". başkan", sep="")