from sklearn.datasets import load_iris


data = load_iris(as_frame=True)

df = data.frame

avg = df.sum(axis = 0)/len(df)

print(avg)
df2 = df['sepal length (cm)']
print(df2)

names = data.target_names

print(names)

setosa = df.iloc[:50]
versicolor = df.iloc[50:100]

print(len(versicolor))