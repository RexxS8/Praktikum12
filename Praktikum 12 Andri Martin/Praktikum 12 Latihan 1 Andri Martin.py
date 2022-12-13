import pandas as pd

data= pd.read_csv("C:/Users/andri/Documents/Andri Martin/Trisakti/Python/Praktikum Algo/Praktikum 12 Latihan 1 Andri Martin/Negara.csv")

df = pd.DataFrame(data)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print(data)
print(mean)
print(std)